#!/usr/bin/env python3
"""
Chatbot pro předmět Matematika (LDF MENDELU).

Skript načte všechny Markdown soubory z tohoto repozitáře a použije
Google Generative AI (Gemini) k zodpovězení otázek na základě obsahu těchto textů.

Použití:
    export GOOGLE_API_KEY="váš_api_klíč"
    python chatbot.py

nebo:
    python chatbot.py --api-key "váš_api_klíč"

Pro získání API klíče navštivte: https://aistudio.google.com/app/apikey
"""

import argparse
import glob
import os
import sys
import textwrap

from google import genai
from google.genai import types


SYSTEM_INSTRUCTION = """Jsi pomocný asistent pro studenty předmětu Matematika na LDF MENDELU.
Odpovídáš na otázky výhradně na základě poskytnutých učebních textů z tohoto předmětu.
Pokud odpověď v textech není, řekni to studentovi a navrhni, kde by mohl hledat.
Odpovídej v češtině, stručně a přesně. Pokud je to vhodné, uveď konkrétní vzorce nebo příklady
z textu."""

MODEL_NAME = "gemini-2.0-flash"
FALLBACK_MODEL_CANDIDATES = (
    "gemini-2.0-flash-lite",
    "gemini-1.5-flash",
    "gemini-1.5-pro",
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
)
# Approximate character limit for the combined knowledge base.  English text
# averages ~4 characters per token; at 900 000 chars the context stays well
# within the Gemini 1.5-Flash 1 M-token window even for Czech text (which is
# slightly more compact per token).
MAX_CONTEXT_CHARS = 900_000


def load_texts(repo_root: str) -> str:
    """Load all Markdown files from the repository and return them as one string."""
    pattern = os.path.join(repo_root, "**", "*.md")
    md_files = sorted(glob.glob(pattern, recursive=True))

    chunks = []
    for path in md_files:
        rel = os.path.relpath(path, repo_root)
        try:
            with open(path, encoding="utf-8") as fh:
                content = fh.read()
            chunks.append(f"## Soubor: {rel}\n\n{content}")
        except OSError as exc:
            print(f"[varování] Nelze načíst {rel}: {exc}", file=sys.stderr)

    combined = "\n\n---\n\n".join(chunks)
    if len(combined) > MAX_CONTEXT_CHARS:
        # Truncate at a paragraph boundary to avoid splitting mid-word or
        # mid-character (important for multi-byte UTF-8 text).
        cutoff = combined.rfind("\n\n", 0, MAX_CONTEXT_CHARS)
        combined = combined[: cutoff if cutoff != -1 else MAX_CONTEXT_CHARS]
        print(
            "[info] Učební texty byly zkráceny kvůli limitu kontextového okna.",
            file=sys.stderr,
        )
    return combined


def _normalize_model_name(model_name: str) -> str:
    return model_name.removeprefix("models/")


def _supports_generate_content(model: types.Model) -> bool:
    """Return True if model looks usable for generate_content calls."""
    name = _normalize_model_name(model.name or "")
    if not name or not name.startswith("gemini"):
        return False
    actions = [action.lower() for action in (model.supported_actions or [])]
    return "generatecontent" in actions


def _is_model_not_found_error(exc: Exception) -> bool:
    """Detect model-not-found across APIError variants."""
    if not isinstance(exc, genai.errors.APIError):
        return False
    # Some responses expose HTTP status code, some expose textual status.
    return (getattr(exc, "code", None) == 404) or (
        getattr(exc, "status", "").upper() == "NOT_FOUND"
    )


def choose_model_name(client: genai.Client, model_name: str) -> tuple[str, list[str]]:
    """Return a valid model name for generate_content and all discovered model names."""
    requested_model = _normalize_model_name(model_name)
    available_names: list[str] = []

    try:
        for model in client.models.list():
            if not _supports_generate_content(model):
                continue
            name = _normalize_model_name(model.name or "")
            available_names.append(name)
    except (genai.errors.APIError, OSError) as exc:
        print(
            f"[varování] Nepodařilo se načíst seznam modelů ({exc}). "
            f"Používám model '{requested_model}' bez automatického fallbacku.",
            file=sys.stderr,
        )
        return requested_model, available_names

    if not available_names:
        return requested_model, available_names

    if requested_model in available_names:
        return requested_model, available_names

    for candidate in FALLBACK_MODEL_CANDIDATES:
        if candidate in available_names:
            return candidate, available_names

    return available_names[0], available_names


def chat_loop(api_key: str, knowledge_base: str, requested_model: str) -> None:
    """Run an interactive question-answering loop using the Gemini API."""
    client = genai.Client(api_key=api_key)
    model_name, available_model_names = choose_model_name(client, requested_model)

    if model_name != _normalize_model_name(requested_model):
        print(
            f"[info] Požadovaný model '{requested_model}' není dostupný, používám '{model_name}'.",
            file=sys.stderr,
        )

    full_system = (
        SYSTEM_INSTRUCTION
        + "\n\n"
        + "=== UČEBNÍ TEXTY ===\n\n"
        + knowledge_base
    )

    config = types.GenerateContentConfig(system_instruction=full_system)
    history: list[types.Content] = []

    print("=" * 60)
    print("Chatbot pro předmět Matematika (LDF MENDELU)")
    print("Napiš svou otázku nebo 'konec' pro ukončení.")
    print("=" * 60)

    while True:
        try:
            question = input("\nOtázka: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nNa shledanou!")
            break

        if not question:
            continue
        if question.lower() in {"konec", "exit", "quit", "q"}:
            print("Na shledanou!")
            break

        history.append(types.Content(role="user", parts=[types.Part(text=question)]))

        try:
            response = client.models.generate_content(
                model=model_name,
                contents=history,
                config=config,
            )
            answer = response.text
        except (genai.errors.APIError, OSError) as exc:
            error_text = str(exc)
            model_not_found = _is_model_not_found_error(exc)
            if model_not_found:
                print(
                    "[chyba] Zvolený model není pro tento API klíč dostupný. "
                    "Použijte parametr --model s modelem dostupným ve vašem účtu.",
                    file=sys.stderr,
                )
                if available_model_names:
                    print(
                        "[info] Dostupné modely: " + ", ".join(sorted(available_model_names)),
                        file=sys.stderr,
                    )
                print(f"[info] Původní chyba: {error_text}", file=sys.stderr)
            else:
                print(f"[chyba] Nepodařilo se získat odpověď: {error_text}", file=sys.stderr)
            history.pop()
            continue

        history.append(
            types.Content(role="model", parts=[types.Part(text=answer)])
        )

        print("\nOdpověď:")
        # Wrap long lines for readability in a terminal
        for paragraph in answer.split("\n"):
            if paragraph:
                print(textwrap.fill(paragraph, width=80))
            else:
                print()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Chatbot pro předmět Matematika používající Google Gemini API."
    )
    parser.add_argument(
        "--api-key",
        default=os.environ.get("GOOGLE_API_KEY", ""),
        help="Google API klíč (výchozí: proměnná prostředí GOOGLE_API_KEY).",
    )
    parser.add_argument(
        "--repo-root",
        default=os.path.dirname(os.path.abspath(__file__)),
        help="Kořenový adresář repozitáře s učebními texty.",
    )
    parser.add_argument(
        "--model",
        default=MODEL_NAME,
        help=(
            "Název Gemini modelu (např. gemini-2.0-flash). "
            f"Výchozí: {MODEL_NAME}."
        ),
    )
    args = parser.parse_args()

    if not args.api_key:
        print(
            "Chyba: Google API klíč nebyl zadán.\n"
            "Nastav proměnnou prostředí GOOGLE_API_KEY nebo použij --api-key.",
            file=sys.stderr,
        )
        sys.exit(1)

    print("Načítám učební texty…", end=" ", flush=True)
    knowledge_base = load_texts(args.repo_root)
    print(f"hotovo ({len(knowledge_base):,} znaků).")

    chat_loop(args.api_key, knowledge_base, args.model)


if __name__ == "__main__":
    main()
