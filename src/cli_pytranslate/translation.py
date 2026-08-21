from collections.abc import Collection

from .config import translator


def translate(
    source: str = "auto",
    target: str = "en",
    text: Collection[str] = "Olá do PyTranslate!",
) -> str:

    translator.source = source
    translator.target = target

    str_text = ""

    for str in text:
        str_text += " "
        str_text += str

    return translator.translate(  # pyright: ignore[reportUnknownMemberType]
        text=str_text
    )
