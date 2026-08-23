from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from textual.widgets import TextArea

from cli_pytranslate.translation import translate


class Translation_Panel(HorizontalGroup):
    """A translation panel"""

    def compose(self) -> ComposeResult:
        self.source = TextArea(placeholder="Type to translate.", id="source")
        self.target = TextArea(
            read_only=True,
            id="target",
            placeholder="Translated text will appear here!",
            highlight_cursor_line=False,
            show_cursor=False,
        )
        yield self.source
        yield self.target

    def get_translation(self) -> str:
        return translate(text=(self.source.text,))

    def set_translated_text(self, text: str) -> None:
        self.target.text = text
        self.target.refresh(repaint=True)
