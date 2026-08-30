from __future__ import annotations

from functools import partial
from typing import TYPE_CHECKING, cast

from textual.command import DiscoveryHit, Hit, Hits, Provider

from cli_pytranslate.config import settings

if TYPE_CHECKING:
    from cli_pytranslate.tui import PyTranslate

# TODO: Improve this to use only two discover commands (change input/output languages)


class LanguageProvider(Provider):
    """A command provider to change the input/output translation languages"""

    @property
    def commands(self) -> list[tuple[str, str, str]]:
        languages = cast(
            dict[str, str],
            settings.default_translator.get_supported_languages(as_dict=True),  # pyright: ignore[reportUnknownMemberType]
        )

        commands: list[tuple[str, str, str]] = []

        for language, lang in languages.items():
            commands.append((language.capitalize(), "source", lang))
            commands.append((language.capitalize(), "target", lang))
        return commands

    async def discover(self) -> Hits:
        for title, panel_id, lang in self.commands:
            yield DiscoveryHit(
                title,
                partial(self.set_language, title, panel_id, lang),
                help=f"Set {panel_id} language to {title.upper().swapcase()}",
            )

    async def search(self, query: str) -> Hits:
        matcher = self.matcher(query)

        for title, panel_id, lang in self.commands:
            match = matcher.match(title)

            if match == 0.0:
                continue

            yield Hit(
                match,
                matcher.highlight(title),
                partial(self.set_language, title, panel_id, lang),
                help=f"Set {panel_id} language to {title.upper().swapcase()}",
            )

    def set_language(self, title: str, panel_id: str, lang: str) -> None:
        app = cast("PyTranslate", self.app)
        app.set_language(lang, panel_id)
        app.refresh_language_title(title, panel_id)
        app.update_translation()
