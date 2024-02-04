import logging
import typer
import rich

from dataclasses import dataclass
from functools import cached_property
from rich.logging import RichHandler


@dataclass
class Application:
    def __post_init__(self):
        logging.basicConfig(
            format="%(message)s",
            datefmt="[%X]",
            handlers=[
                RichHandler(
                    console=self.console,
                    rich_tracebacks=True,
                    show_path=False,
                )
            ],
        )

    @cached_property
    def typer_app(self):
        return typer.Typer()

    @cached_property
    def console(self):
        return rich.console.Console(
            log_path=False,
        )
