import click.testing
import pytest

from hyper_python import console

@pytest.fixture
def runner():
    return click.testing.CliRunner()

@pytest.fixture
def mock_request_get(mocker):
    mock = mocker.patch("hyper_python.console.requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Mathilde Laigle",
        "extract": "Mathilde Laigle (1865–1949) was a French historian. She was an early student in America becoming a governess to the children of the governor of Iowa. She was an expert on Christine de Pizan and is credited with helping to revive interest in the early feminist.",
        "thumbnail": {
            "source": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Mathilde_Laigle_portrait_de_Gu%C3%A9rin.jpg/320px-Mathilde_Laigle_portrait_de_Gu%C3%A9rin.jpg"
        }
    }
    return mock

def test_console(runner, mock_request_get):
    result = runner.invoke(console.main)
    assert result.exit_code == 0
    assert len(result.output) > 0
    assert "Mathilde Laigle" in result.output

def test_main_invokes_request_get(runner, mock_request_get):
    runner.invoke(console.main)
    assert mock_request_get.called

def test_main_uses_wikimedia_org(runner, mock_request_get):
    runner.invoke(console.main)
    args, _ = mock_request_get.call_args
    assert "wikimedia.org" in args[0]
