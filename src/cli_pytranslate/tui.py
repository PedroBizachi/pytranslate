from typing import cast

from textual import on
from textual.app import App, ComposeResult
from textual.timer import Timer
from textual.widgets import Button, Footer, TextArea
from textual.worker import Worker, WorkerState

from cli_pytranslate.command_palette import LanguageProvider
from cli_pytranslate.config import settings
from cli_pytranslate.widgets.custom_header import Custom_Header
from cli_pytranslate.widgets.translation_panel import Translation_Panel


class PyTranslate(App):  # pyright: ignore[reportMissingTypeArgument]
    _translation_timer: Timer | None = None
    CSS_PATH = "tui.scss"

    COMMANDS = App.COMMANDS | {LanguageProvider}

    AUTO_FOCUS = "#source"

    BINDINGS = [
        # TODO: Change ctrl+d to ctrl+c
        # TODO: ctrl+ENTER to apply translation
        # ("tab", "switch_panels", "Switch translation panels"),
        # Needs to be dinamic, on settings tab must have "Go to translate" description
        # ("ctrl+s", "switch_tabs", "Go to settings"),
        ("c", "copy_translated_text", "Copy translated text"),
        # TODO: Remove ctrl+enter add a new line on textarea
        ("ctrl+enter", "quick_submit_translation", "Submit translation"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Custom_Header()
        yield Translation_Panel(id="translate-panel")
        yield Footer()

    # === ACTIONS ===

    def action_copy_translated_text(self) -> None:
        self.notify("Translated text copied to clipboard!")

    def action_quick_submit_translation(self) -> None:
        self.query_one("#submit", Button).action_press()

    # === EVENTS ===

    @on(Button.Pressed, "#submit")
    def on_submit_pressed(self) -> None:
        self.update_translation()

    @on(TextArea.Changed, "#source")
    def on_text_area_changed(self) -> None:
        if self._translation_timer is not None:
            self._translation_timer.stop()

        self._translation_timer = self.set_timer(0.5, self.update_translation)

    # Handle worker related to the translation
    def on_worker_state_changed(self, event: Worker.StateChanged) -> None:
        button = self.query_one("#submit", Button)
        panel = self.query_one("#translate-panel", Translation_Panel)

        worker = cast(Worker[str], event.worker)

        if worker.state == WorkerState.SUCCESS:
            panel.set_translated_text(worker.result)
            button.loading = False
            button.styles.color = self.theme_variables.get("text-success")
            button.styles.border = (
                "round",
                f"{self.theme_variables.get('text-success')}",
            )
        elif worker.state == WorkerState.ERROR:
            panel.set_translated_text(panel.source.text)
            self.notify(f"Error: {worker.error}", severity="error")
            button.loading = False
            button.styles.color = self.theme_variables.get("text-error")
            button.styles.border = (
                "round",
                f"{self.theme_variables.get('text-error')}",
            )

    # === METHODS ===

    # Create worker to hot-update output translation
    def update_translation(self) -> None:
        button = self.query_one("#submit", Button)
        panel = self.query_one("#translate-panel", Translation_Panel)

        button.loading = True

        self.run_worker(
            panel.get_translation, exclusive=True, thread=True, exit_on_error=False
        )

    # Get the actual selected input/output translation languages
    def get_language(self, panel_id: str, full: bool = False) -> str:
        if full:
            if panel_id == "source":
                return settings.DEFAULT_SOURCE_TITLE
            if panel_id == "target":
                return settings.DEFAULT_TARGET_TITLE

        if panel_id == "source":
            return settings.DEFAULT_SOURCE
        if panel_id == "target":
            return settings.DEFAULT_TARGET
        raise ValueError(f"Unknown panel id: {panel_id}")

    # Set the selected language for input or output
    def set_language(self, lang: str, panel_id: str) -> None:
        if panel_id == "source":
            settings.DEFAULT_SOURCE = lang
        elif panel_id == "target":
            settings.DEFAULT_TARGET = lang
        else:
            raise ValueError(f"Unknown panel id: {panel_id}")

    # Set border titles after UI initialization
    def refresh_language_title(
        self,
        title: str | None = None,
        panel_id: str | None = None,
        default: bool = False,
    ) -> None:
        if default:
            self.query_one(
                "#source", TextArea
            ).border_title = settings.DEFAULT_SOURCE_TITLE
            self.query_one(
                "#target", TextArea
            ).border_title = settings.DEFAULT_TARGET_TITLE
            return

        self.query_one(f"#{panel_id}", TextArea).border_title = title

    def on_mount(self) -> None:
        self.refresh_language_title(default=True)


def main():
    app = PyTranslate()
    app.run()
