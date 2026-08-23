from textual.app import ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Label

from cli_pytranslate.config import settings
from cli_pytranslate.widgets.submit_button import Submit_button


class Custom_Header(Container):
    """A custom header"""

    def compose(self) -> ComposeResult:
        self.engine = Label(
            f"Engine: {settings.default_translator_name}",
            id="engine",
        )
        with Horizontal(id="main-row"):
            yield self.engine
            yield Submit_button(id="submit")
