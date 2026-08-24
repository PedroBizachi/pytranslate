from typing import cast

from textual import on
from textual.app import App, ComposeResult
from textual.timer import Timer
from textual.widgets import Button, Footer, TextArea
from textual.worker import Worker, WorkerState

from cli_pytranslate.widgets.custom_header import Custom_Header
from cli_pytranslate.widgets.translation_panel import Translation_Panel


class PyTranslate(App):  # pyright: ignore[reportMissingTypeArgument]
    _translation_timer: Timer | None = None
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
    def on_submit_pressed(self) -> None:
        self.update_translation()

    @on(TextArea.Changed, "#source")
    def on_text_area_changed(self) -> None:
        if self._translation_timer is not None:
            self._translation_timer.stop()

        self._translation_timer = self.set_timer(0.5, self.update_translation())

    def update_translation(self) -> None:
        button = self.query_one("#submit", Button)
        panel = self.query_one("#translate-panel", Translation_Panel)

        button.loading = True

        self.run_worker(
            panel.get_translation, exclusive=True, thread=True, exit_on_error=False
        )

    def on_worker_state_changed(self, event: Worker.StateChanged) -> None:
        button = self.query_one("#submit", Button)
        panel = self.query_one("#translate-panel", Translation_Panel)

        worker = cast(Worker[str], event.worker)

        if worker.state == WorkerState.SUCCESS:
            panel.set_translated_text(worker.result)
            button.loading = False
        elif worker.state == WorkerState.ERROR:
            self.notify(f"Error: {worker.error}", severity="error")
            button.loading = False


def main():
    app = PyTranslate()
    app.run()
