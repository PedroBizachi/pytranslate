from __future__ import annotations

from functools import partial
from typing import TYPE_CHECKING, cast

from textual.command import CommandPalette, DiscoveryHit, Hit, Hits, Provider

from pytranslate_tui.config import settings

if TYPE_CHECKING:
    from pytranslate_tui.tui import PyTranslate


class LanguageProvider(Provider):
    """A command provider to change the input/output translation languages"""

    async def discover(self) -> Hits:
        yield DiscoveryHit(
            "Change input language",
            self.open_input_language_mode,
            help="Select the source language for translation.",
        )
        yield DiscoveryHit(
            "Change output language",
            self.open_output_language_mode,
            help="Select the target language for translation.",
        )

    async def search(self, query: str) -> Hits:
        matcher = self.matcher(query)

        commands = [
            (
                "Change input language",
                self.open_input_language_mode,
                "Select the source language for translation.",
            ),
            (
                "Change output language",
                self.open_output_language_mode,
                "Select the target language for translation.",
            ),
        ]

        for text, action, help_text in commands:
            score = matcher.match(text)
            if score > 0:
                yield Hit(
                    score,
                    matcher.highlight(text),
                    action,
                    help=help_text,
                )

    def open_input_language_mode(self) -> None:
        self.app.push_screen(CommandPalette(providers=[InputLanguageProvider]))

    def open_output_language_mode(self) -> None:
        self.app.push_screen(CommandPalette(providers=[OutputLanguageProvider]))


class OutputLanguageProvider(Provider):
    async def discover(self) -> Hits:
        for language, lang in self.commands:
            yield DiscoveryHit(
                display=language,
                command=partial(self.set_language, language, "target", lang),
            )

    async def search(self, query: str) -> Hits:
        matcher = self.matcher(query)
        for language, lang in self.commands:
            score = matcher.match(language)
            if score > 0:
                yield Hit(
                    score,
                    matcher.highlight(language),
                    command=partial(self.set_language, language, "target", lang),
                )

    @property
    def commands(self) -> list[tuple[str, str]]:
        languages = cast(
            dict[str, str],
            settings.translator.get_supported_languages(as_dict=True),  # pyright: ignore[reportUnknownMemberType]
        )

        commands: list[tuple[str, str]] = []

        if "Lingue" in settings.translator_name:
            for language, lang in languages.items():
                commands.append((language.capitalize(), language))

        if "Pons" in settings.translator_name:
            for lang, language in languages.items():
                commands.append((language.capitalize(), lang))
        else:
            for language, lang in languages.items():
                commands.append((language.capitalize(), lang))
        return commands

    def set_language(self, title: str, panel_id: str, lang: str) -> None:
        app = cast("PyTranslate", self.app)
        app.set_language(lang, panel_id)
        app.refresh_language_title(title, panel_id)
        app.update_translation()


class InputLanguageProvider(Provider):
    async def discover(self) -> Hits:
        for language, lang in self.commands:
            yield DiscoveryHit(
                display=language,
                command=partial(self.set_language, language, "source", lang),
            )

    async def search(self, query: str) -> Hits:
        matcher = self.matcher(query)
        for language, lang in self.commands:
            score = matcher.match(language)
            if score > 0:
                yield Hit(
                    score,
                    matcher.highlight(language),
                    command=partial(self.set_language, language, "source", lang),
                )

    @property
    def commands(self) -> list[tuple[str, str]]:
        languages = cast(
            dict[str, str],
            settings.translator.get_supported_languages(as_dict=True),  # pyright: ignore[reportUnknownMemberType]
        )

        commands: list[tuple[str, str]] = []

        if "Lingue" in settings.translator_name:
            for language, lang in languages.items():
                commands.append((language.capitalize(), language))

        if "Pons" in settings.translator_name:
            for lang, language in languages.items():
                commands.append((language.capitalize(), lang))
        else:
            for language, lang in languages.items():
                commands.append((language.capitalize(), lang))
        return commands

    def set_language(self, title: str, panel_id: str, lang: str) -> None:
        app = cast("PyTranslate", self.app)
        app.set_language(lang, panel_id)
        app.refresh_language_title(title, panel_id)
        app.update_translation()
