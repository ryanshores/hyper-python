from hyper_python import wikipedia
from . import LANG_DE, WIKI_URL


def test_language(mock_requests_get):
    wikipedia.random_page()
    args, _ = mock_requests_get.call_args
    assert WIKI_URL.format(language=LANG_DE) in args[0]
