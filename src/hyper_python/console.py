import click
import textwrap

from . import __version__, wikipedia, asciiHelper


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
    click.echo(asciiHelper.convert_image_url_to_ascii(thumbnail))
