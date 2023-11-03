
import feedparser
from commitgpt import  __VERSION__
import sys
import os
from rich import print
import typer

RELEASE_FEED_URL = "https://pypi.org/rss/project/commitgpt/releases.xml"
INSTALL_COMMAND = "pip install --break-system-packages --upgrade commitgpt"


def check_update() -> bool:
    """
    `check_update` checks if there is a new version of commitgpt available.

    Args:
        None

    Returns:
        bool: True if there is a new version of commitgpt available,
        False otherwise.
    """
    feed = feedparser.parse(RELEASE_FEED_URL)
    releases = []
    for entry in feed["entries"]:
        releases.append(entry["title"])
    latest_release = max(releases)

    return latest_release != __VERSION__


def update() -> None:
    """
    `Update` commitgpt.

    Args:
        None

    Returns:
        None
    """
    os.system(f"{sys.executable} -m {INSTALL_COMMAND}")


def check_and_update() -> None:
    """
    `check_and_update` checks if there is a new version of commitgpt available.
    If there is, it prompts the user to update.

    Args:
        None

    Returns:
        None
    """
    if check_update():
        print("[bold green]New version of commitgpt available[/bold green]")
        ok = typer.confirm(
            text="Do you want to update?",
            default=True,
            show_default=True,
        )
        if ok:
            update()
            print("[bold green]Updated commitgpt![/bold green]")
            return None

    return None
