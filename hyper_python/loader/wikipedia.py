import click
import requests

from .. import LANG_EN, WIKI_API_URL


def random_page(language=LANG_EN):
    API_URL = WIKI_API_URL.format(language=language)
    try:
        with requests.get(API_URL) as response:
            response.raise_for_status()
            return response.json()
    except requests.RequestException as error:
        message = str(error)
        raise click.ClickException(message)
