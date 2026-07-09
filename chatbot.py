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

MODEL_NAME = "gemini-1.5-flash"
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


def chat_loop(api_key: str, knowledge_base: str) -> None:
    """Run an interactive question-answering loop using the Gemini API."""
    client = genai.Client(api_key=api_key)

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
                model=MODEL_NAME,
                contents=history,
                config=config,
            )
            answer = response.text
        except (genai.errors.APIError, OSError) as exc:
            print(f"[chyba] Nepodařilo se získat odpověď: {exc}", file=sys.stderr)
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

    chat_loop(args.api_key, knowledge_base)


if __name__ == "__main__":
    main()
