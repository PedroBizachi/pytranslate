from typing import cast

from textual import on
from textual.app import ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Label, Select

from cli_pytranslate.config import settings
from cli_pytranslate.widgets.submit_button import Submit_button


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

    @on(Select.Changed)
    def select_changed(self, event: Select.Changed) -> None:
        translator = cast(str, event.value)
        settings.set_default_translator(translator)
