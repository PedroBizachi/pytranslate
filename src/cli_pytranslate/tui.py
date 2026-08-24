from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button, Footer, TextArea

from cli_pytranslate.translation import translate
from cli_pytranslate.widgets.custom_header import Custom_Header
from cli_pytranslate.widgets.translation_panel import Translation_Panel


class PyTranslate(App):  # pyright: ignore[reportMissingTypeArgument]
    CSS_PATH = "tui.css"

    BINDINGS = [
        # TODO: Change ctrl+d to ctrl+c
        # TODO: ctrl+ENTER to apply translation
        ("tab", "switch_panels", "Switch translation panels"),
        # Needs to be dinamic, on settings tab must have "Go to translate" description
        ("ctrl+s", "switch_tabs", "Go to settings"),
        ("c", "copy_translated_text", "Copy translated text"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Custom_Header()
        yield Translation_Panel(id="translate-panel")
        yield Footer()

    def action_copy_translated_text(self) -> None:
        self.notify("Translated text copied to clipboard!")

    @on(Button.Pressed, "#submit")
    @on(TextArea.Changed, "#source")
    def update_translation(self) -> None:
        button = self.query_one("#submit", Button)
        button.loading = True
        panel = self.query_one("#translate-panel", Translation_Panel)
        try:
            translated_text = translate(text=(panel.source.text,))

            panel.target.text = translated_text
            panel.target.refresh(repaint=True)
        finally:
            button.loading = False


def main():
    app = PyTranslate()
    app.run()
