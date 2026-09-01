from __future__ import annotations

from typing import TYPE_CHECKING, cast

from textual import on
from textual.app import ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Label, Select

from cli_pytranslate.config import settings
from cli_pytranslate.widgets.submit_button import Submit_button

if TYPE_CHECKING:
    from cli_pytranslate.tui import PyTranslate


class Custom_Header(Horizontal):
    """A custom header"""

    def compose(self) -> ComposeResult:
        yield Label("Engine:", id="engine-label")
        yield Select(
            options=settings.get_available_translators(),
            value=settings.get_available_translators()[0][1],
            id="engine",
        )
        with Container(id="app-title-container"):
            yield Label("PyTranslate", id="app-title")
        yield Submit_button(id="submit")

    @on(Select.Changed, "#engine")
    def select_changed(self, event: Select.Changed) -> None:
        app = cast("PyTranslate", self.app)
        translator = cast(str, event.value)

        if "Lingue" in translator or "Pons" in translator:
            self.notify(
                "This engine doesn't support 'auto' language detection. Input language set to 'english'.",
                severity="warning",
            )
            app.set_language("english", "source")
            app.refresh_language_title("English", "source")

        settings.set_default_translator(translator)
