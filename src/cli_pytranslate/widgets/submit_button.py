from textual.app import ComposeResult
from textual.widgets import Button


class Submit_button(Button):
    def compose(self) -> ComposeResult:
        self.label = "TRANSLATE"
        self.flat = True
        return super().compose()
