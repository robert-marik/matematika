#!/usr/bin/env python3
"""
Chatbot pro předmět Matematika (LDF MENDELU).

Skript načte všechny Markdown soubory z tohoto repozitáře, rozdělí je na sekce
a pro každý dotaz vybere jen nejrelevantnější části textu, které pak vloží do
promptu modelu Google Generative AI (Gemini).  Tím se chatbot nezadrhne ani
v případě, že je materiálů více, než by se vešlo do kontextového okna.

Použití:
    export GOOGLE_API_KEY="váš_api_klíč"
    python chatbot.py

nebo:
    python chatbot.py --api-key "váš_api_klíč"

Pro získání API klíče navštivte: https://aistudio.google.com/app/apikey
"""

import argparse
import dataclasses
import glob
import os
import re
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

# Per-query retrieval limits: take up to this many sections and this many
# characters of source text for each question.  This keeps every prompt
# at a predictable, model-friendly size regardless of corpus size.
MAX_RETRIEVED_SECTIONS = 6
MAX_RETRIEVED_CHARS = 60_000

# Keep only the last N turns of conversation history so that the context
# window is not filled by old exchanges at the expense of retrieved content.
MAX_HISTORY_TURNS = 6

# Minimum number of characters worth including when a section is truncated to
# fit the remaining char budget.  Shorter snippets would be too small to be
# useful context for the model.
MIN_TRUNCATED_SECTION_CHARS = 200


@dataclasses.dataclass(frozen=True)
class Section:
    """One logical chunk of a Markdown source file."""

    source: str   # relative path of the markdown file
    heading: str  # heading text (or filename for preamble sections)
    content: str  # full section text including the heading line


def load_sections(repo_root: str) -> list[Section]:
    """Load all Markdown files and split them into sections by headings."""
    pattern = os.path.join(repo_root, "**", "*.md")
    md_files = sorted(glob.glob(pattern, recursive=True))

    heading_re = re.compile(r"^#{1,6}\s+(.+)", re.MULTILINE)
    sections: list[Section] = []

    for path in md_files:
        rel = os.path.relpath(path, repo_root)
        try:
            with open(path, encoding="utf-8") as fh:
                content = fh.read()
        except OSError as exc:
            print(f"[varování] Nelze načíst {rel}: {exc}", file=sys.stderr)
            continue

        # Find all heading positions and their text
        splits = [(m.start(), m.group(1)) for m in heading_re.finditer(content)]

        if not splits:
            # No headings — treat whole file as one section
            if content.strip():
                sections.append(Section(source=rel, heading=rel, content=content))
            continue

        # Text before first heading (preamble)
        if splits[0][0] > 0:
            preamble = content[: splits[0][0]].strip()
            if preamble:
                sections.append(Section(source=rel, heading=rel, content=preamble))

        for i, (pos, heading) in enumerate(splits):
            end = splits[i + 1][0] if i + 1 < len(splits) else len(content)
            section_text = content[pos:end].strip()
            if section_text:
                sections.append(Section(source=rel, heading=heading, content=section_text))

    return sections


def _tokenize(text: str) -> set[str]:
    """Return a set of lowercase word tokens.

    Tokens of length 1 and above are kept to preserve short but significant
    mathematical notation such as 'pi', 'dx', 'dy', or single-letter variables.
    Empty strings produced by the split are discarded.
    """
    return {w.lower() for w in re.split(r"\W+", text) if w}


def find_relevant_sections(
    sections: list[Section],
    query: str,
    max_sections: int = MAX_RETRIEVED_SECTIONS,
    max_chars: int = MAX_RETRIEVED_CHARS,
) -> list[Section]:
    """Return the most relevant sections for *query* using keyword overlap scoring."""
    query_tokens = _tokenize(query)
    if not query_tokens:
        return sections[:max_sections]

    scored: list[tuple[int, int, Section]] = []
    for idx, section in enumerate(sections):
        text_tokens = _tokenize(section.heading + " " + section.content)
        score = len(query_tokens & text_tokens)
        if score > 0:
            scored.append((score, idx, section))

    # Best score first; for equal scores keep original document order
    scored.sort(key=lambda x: (-x[0], x[1]))

    result: list[Section] = []
    total_chars = 0
    for _, _, section in scored:
        if len(result) >= max_sections:
            break
        remaining = max_chars - total_chars
        if remaining <= 0:
            break
        if len(section.content) > remaining:
            # Include a truncated version rather than nothing when it is
            # the first (best) section and there is still reasonable space.
            # Truncate at the last whitespace to avoid splitting mid-word.
            if not result and remaining > MIN_TRUNCATED_SECTION_CHARS:
                truncated = section.content[:remaining]
                cutoff = truncated.rfind(" ")
                if cutoff > MIN_TRUNCATED_SECTION_CHARS:
                    truncated = truncated[:cutoff]
                result.append(dataclasses.replace(section, content=truncated))
            break
        result.append(section)
        total_chars += len(section.content)

    return result


def _build_context_text(sections: list[Section]) -> str:
    """Format retrieved sections as a context block to prepend to the query."""
    if not sections:
        return ""
    parts = [
        f"### Zdroj: {sec.source} — {sec.heading}\n\n{sec.content}"
        for sec in sections
    ]
    return "=== RELEVANTNÍ ČÁSTI UČEBNÍCH TEXTŮ ===\n\n" + "\n\n---\n\n".join(parts)


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
    return (getattr(exc, "code", None) == 404) or (
        getattr(exc, "status", "").upper() == "NOT_FOUND"
    )


def _is_quota_exceeded_error(exc: Exception) -> bool:
    """Detect quota/rate-limit errors across APIError variants."""
    if not isinstance(exc, genai.errors.APIError):
        return False
    if getattr(exc, "code", None) == 429 or (
        getattr(exc, "status", "").upper() == "RESOURCE_EXHAUSTED"
    ):
        return True
    return "quota exceeded" in str(exc).lower()


def _extract_retry_seconds(error_text: str) -> float | None:
    """Extract retry delay from API error text if present."""
    match = re.search(r"retry in ([0-9]+(?:\.[0-9]+)?)s", error_text, flags=re.IGNORECASE)
    if not match:
        return None
    return float(match.group(1))


def _quota_fallback_models(
    current_model: str, available_model_names: list[str]
) -> list[str]:
    """Return ordered fallback candidates when current model hits quota limits."""
    current = _normalize_model_name(current_model)
    normalized_available = {
        _normalize_model_name(name) for name in available_model_names if name
    }
    normalized_available.discard("")

    if normalized_available:
        candidates = [
            _normalize_model_name(name)
            for name in FALLBACK_MODEL_CANDIDATES
            if _normalize_model_name(name) in normalized_available
        ]
        for model in sorted(normalized_available):
            if model not in candidates:
                candidates.append(model)
    else:
        candidates = [_normalize_model_name(name) for name in FALLBACK_MODEL_CANDIDATES]

    result: list[str] = []
    seen = {current}
    for candidate in candidates:
        if not candidate or candidate in seen:
            continue
        seen.add(candidate)
        result.append(candidate)
        if len(result) >= 5:
            break
    return result


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


def chat_loop(api_key: str, sections: list[Section], requested_model: str) -> None:
    """Run an interactive question-answering loop using the Gemini API."""
    client = genai.Client(api_key=api_key)
    model_name, available_model_names = choose_model_name(client, requested_model)

    if model_name != _normalize_model_name(requested_model):
        print(
            f"[info] Požadovaný model '{requested_model}' není dostupný, používám '{model_name}'.",
            file=sys.stderr,
        )

    config = types.GenerateContentConfig(system_instruction=SYSTEM_INSTRUCTION)
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

        # Retrieve relevant sections for this question
        relevant = find_relevant_sections(sections, question)
        context_text = _build_context_text(relevant)

        if context_text:
            user_text = context_text + "\n\n=== OTÁZKA ===\n\n" + question
        else:
            user_text = (
                question
                + "\n\n(Poznámka: V učebních textech nebyla nalezena žádná "
                "přímo relevantní pasáž k tomuto dotazu.)"
            )

        history.append(types.Content(role="user", parts=[types.Part(text=user_text)]))

        answer = None
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
            quota_exceeded = _is_quota_exceeded_error(exc)
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
            elif quota_exceeded:
                switched = False
                hard_failure = False
                for fallback_model in _quota_fallback_models(
                    model_name, available_model_names
                ):
                    try:
                        response = client.models.generate_content(
                            model=fallback_model,
                            contents=history,
                            config=config,
                        )
                        answer = response.text
                        previous_model = model_name
                        model_name = fallback_model
                        switched = True
                        print(
                            f"[info] Model '{previous_model}' měl vyčerpanou kvótu, "
                            f"přepínám na '{fallback_model}'.",
                            file=sys.stderr,
                        )
                        break
                    except (genai.errors.APIError, OSError) as fallback_exc:
                        if _is_quota_exceeded_error(fallback_exc) or _is_model_not_found_error(fallback_exc):
                            continue
                        print(
                            f"[chyba] Nepodařilo se získat odpověď: {fallback_exc}",
                            file=sys.stderr,
                        )
                        hard_failure = True
                        break

                if not switched and not hard_failure:
                    print(
                        f"[chyba] Kvóta pro model '{model_name}' je vyčerpaná "
                        "nebo není pro tento účet dostupná.",
                        file=sys.stderr,
                    )
                    if available_model_names:
                        print(
                            "[info] Dostupné modely: "
                            + ", ".join(sorted(available_model_names)),
                            file=sys.stderr,
                        )
                    retry_seconds = _extract_retry_seconds(error_text)
                    if retry_seconds:
                        print(
                            f"[info] API doporučuje opakovat dotaz za ~{retry_seconds:.1f} s.",
                            file=sys.stderr,
                        )
                    print(
                        "[info] Pokud se chyba opakuje, použijte jiný model "
                        "(--model ...) nebo zkontrolujte kvóty/billing v Google AI Studio.",
                        file=sys.stderr,
                    )
            else:
                print(f"[chyba] Nepodařilo se získat odpověď: {error_text}", file=sys.stderr)
            if answer is None:
                history.pop()
                continue

        history.append(
            types.Content(role="model", parts=[types.Part(text=answer)])
        )

        # Keep history bounded: trim to MAX_HISTORY_TURNS messages so the
        # context window is not filled by old exchanges at the expense of
        # retrieved content.  Trim after both user and model messages are
        # added so the limit is enforced consistently between iterations.
        if len(history) > MAX_HISTORY_TURNS:
            history = history[-MAX_HISTORY_TURNS:]

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
    sections = load_sections(args.repo_root)
    print(f"hotovo ({len(sections)} sekcí).")

    chat_loop(args.api_key, sections, args.model)


if __name__ == "__main__":
    main()
