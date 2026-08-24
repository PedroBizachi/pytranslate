from collections.abc import Collection

from cli_pytranslate.config import settings, translator


def translate(
    source: str = settings.DEFAULT_SOURCE,
    target: str = settings.DEFAULT_TARGET,
    text: Collection[str] | None = "Olá do PyTranslate!",
) -> str:

    if not isinstance(text, Collection) or not text or len(text) == 0:
        raise ValueError("Please provide some text to be translated")

    translator.source = source
    translator.target = target

    str_text = ""

    for str in text:
        str_text += " "
        str_text += str

    result = ""

    try:
        result = translator.translate(  # pyright: ignore[reportUnknownMemberType]
            text=str_text
        )
    except Exception as e:
        raise e

    return result
