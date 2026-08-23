from textual.app import App, ComposeResult
from textual.widgets import Footer

from cli_pytranslate.widgets.custom_header import Custom_Header
from cli_pytranslate.widgets.submit_button import Submit_button
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

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


def main():
    app = PyTranslate()
    app.run()
