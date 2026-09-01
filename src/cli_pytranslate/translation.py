from collections.abc import Collection

from cli_pytranslate.config import settings


def translate(
    source: str = settings.source,
    target: str = settings.target,
    text: Collection[str] | None = "Olá do PyTranslate!",
) -> str:

    if not isinstance(text, Collection) or not text or len(text) == 0:
        raise ValueError("Please provide some text to be translated")

    settings.translator.source = source
    settings.translator.target = target

    str_text = ""

    for str in text:
        str_text += " "
        str_text += str

    result = ""

    try:
        result = settings.translator.translate(text=str_text)  # pyright: ignore[reportUnknownMemberType]
    except Exception as e:
        raise e

    return result
