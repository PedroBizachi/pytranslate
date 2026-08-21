from collections.abc import Collection

from cli_pytranslate.config import settings, translator


def translate(
    source: str = settings.DEFAULT_SOURCE,
    target: str = settings.DEFAULT_TARGET,
    text: Collection[str] = "Olá do PyTranslate!",
) -> str:

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
