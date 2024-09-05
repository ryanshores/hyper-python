import click
import textwrap

from . import __version__
from .loader import wikipedia
from .helper import datetime_helper, ascii_helper
from .ercot import service as ercot_service


@click.command()
@click.option('--language', '-l', default='en', help="Language edition of Wikipedia", metavar='LANG', show_default=True)
@click.version_option(version=__version__)
def main(language):
    """The hyper python project."""
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

        time = energy_mix.get_time()
        total_generation = energy_mix.get_total_generation()
        total_renewable_generation = energy_mix.get_renewable_generation()
        renewable_percentage = energy_mix.get_renewable_percentage()

        click.secho(time, fg="blue")

        click.secho(f"Total Gen: {total_generation:.1f} MW", fg="red")
        click.secho(f"Renewable Gen: {total_renewable_generation:.1f} MW", fg="green")
        click.secho(f"Renewable Mix: {renewable_percentage:.1f}%", fg="yellow")
    except Exception as error:
        message = str(error)
        raise click.ClickException(message)