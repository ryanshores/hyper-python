"""
This module contains command-line interface (CLI) commands for interacting with Wikipedia
and ERCOT data services. The commands make use of the Click library for managing command-line
options and arguments. The Wikipedia command fetches a random page from the specified language
edition of Wikipedia, while the ERCOT command retrieves and displays the current energy mix data.
"""

import textwrap
from datetime import datetime
import click

from . import __version__, DATETIME_FORMAT
from .loader import wikipedia
from .helper import ascii_helper
from .ercot import service as ercot_service


@click.command()
@click.option('--language', '-l',
              default='en',
              help="Language edition of Wikipedia",
              metavar='LANG',
              show_default=True)
@click.version_option(version=__version__)
def main(language):
    """
    :param language: Language edition of Wikipedia
    :return: None
    """
    data = wikipedia.random_page(language=language)

    title = data["title"]
    extract = data["extract"]
    thumbnail = data["thumbnail"]["source"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
    click.echo(ascii_helper.convert_image_url_to_ascii(thumbnail))


@click.command()
@click.version_option(version=__version__)
def ercot_command():
    """Ercot data loader.."""
    try:
        energy_mix = ercot_service.get_energy_mix()

        time = datetime.strptime(energy_mix.get_time(), DATETIME_FORMAT).strftime(
            "%I:%M %p"
        )
        total_generation = energy_mix.get_total_generation()
        total_renewable_generation = energy_mix.get_renewable_generation()
        renewable_percentage = energy_mix.get_renewable_percentage()

        rounded_pct = int(renewable_percentage // 5)
        if renewable_percentage > 90:
            color = 'green'
        elif renewable_percentage > 50:
            color = 'yellow'
        else:
            color = 'red'

        click.secho("Fuel mix as of " + time, fg="blue", bold=True)
        mix_bar = f"Renewable Mix: [{'⚡' * rounded_pct}{'-' * (20 - rounded_pct)}] "
        mix_text = f"{total_renewable_generation:.0f}/{total_generation:.0f} "
        mix_pct_text = f"({renewable_percentage:.1f}%)"
        click.secho(mix_bar + mix_text + mix_pct_text, fg=color)
    except Exception as error:
        message = str(error)
        raise click.ClickException(message)
