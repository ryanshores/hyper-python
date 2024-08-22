import click
import requests
import textwrap

from . import __version__
from . import image_to_ascii_converter

API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"

@click.command()
@click.version_option(version=__version__)
def main():
    """The hyper python project."""
    with requests.get(API_URL) as response:
        response.raise_for_status()
        data = response.json()

    title = data["title"]
    extract = data["extract"]
    thumbnail = data["thumbnail"]["source"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
    click.echo(image_to_ascii_converter.convert_image_url_to_ascii(thumbnail))
