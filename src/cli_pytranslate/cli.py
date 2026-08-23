import logging
from collections.abc import Collection

import click
from rich.logging import RichHandler

from cli_pytranslate.config import settings
from cli_pytranslate.translation import translate

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        RichHandler(
            show_path=False,
        )
    ],
)

logger = logging.getLogger(__name__)


@click.command(context_settings={"ignore_unknown_options": True})
@click.option("-v", "--verbose", is_flag=True, help="Enable verbose mode")
@click.option(
    "-s",
    "source",
    default=settings.DEFAULT_SOURCE,
    required=False,
    nargs=1,
    help=f"Provide the source language to be translated from. Defaults to {settings.DEFAULT_SOURCE}.",
)
@click.option(
    "-t",
    "target",
    default=settings.DEFAULT_TARGET,
    required=False,
    nargs=1,
    help=f"Provide the target language to be translated to. Defaults to {settings.DEFAULT_TARGET}",
)
@click.argument("text", nargs=-1)
def main(source: str, target: str, text: Collection[str], verbose: bool):
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Verbose logging enabled.")

    logger.debug(f"Received source: {source}")
    logger.debug(f"Received target: {target}")

    logger.debug(f"Translating from {source} to {target}.")

    translated_text = translate(source=source, target=target, text=text)

    click.echo(translated_text)
