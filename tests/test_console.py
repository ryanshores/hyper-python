import click.testing
import pytest
import requests

from hyper_python import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()

@pytest.fixture
def mock_wiki_page(mocker):
    return mocker.patch('hyper_python.loader.wikipedia.random_page')


def test_console(runner, mock_requests_get):
    result = runner.invoke(console.main)
    assert result.exit_code == 0
    assert len(result.output) > 0
    assert "Mathilde Laigle" in result.output


def test_main_invokes_request_get(runner, mock_requests_get):
    runner.invoke(console.main)
    assert mock_requests_get.called


def test_main_uses_wikimedia_org(runner, mock_requests_get):
    runner.invoke(console.main)
    args, _ = mock_requests_get.call_args
    assert "wikimedia.org" in args[0]


def test_main_fails_on_request_error(runner, mock_requests_get):
    mock_requests_get.side_effect = Exception('Boom')
    result = runner.invoke(console.main)
    assert result.exit_code == 1


def test_main_prints_error_on_request_error(runner, mock_requests_get):
    mock_requests_get.side_effect = requests.RequestException
    result = runner.invoke(console.main)
    assert 'Error' in result.output


def test_with_language(runner, mock_wiki_page):
    runner.invoke(console.main, ['--language', 'pl'])
    mock_wiki_page.assert_called_with(language='pl')

def test_ercot_fuel_mix(runner):
    result = runner.invoke(console.ercot_command)
    assert result.exit_code == 0

