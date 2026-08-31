from typing import cast

from textual import on
from textual.app import ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Select

from cli_pytranslate.config import settings
from cli_pytranslate.widgets.submit_button import Submit_button


class Custom_Header(Container):
    """A custom header"""

    def compose(self) -> ComposeResult:
        self.engine_list = Select(
            options=settings.get_available_translators(),
            value=settings.get_available_translators()[0][1],
            id="engine",
            compact=True,
        )
        with Horizontal(id="main-row"):
            yield self.engine_list
            yield Submit_button(id="submit")

    @on(Select.Changed)
    def select_changed(self, event: Select.Changed) -> None:
        translator = cast(str, event.value)
        settings.set_default_translator(translator)
