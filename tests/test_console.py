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
        "title": "Mathilde Laigle (1865–1949)",
        "extract": "Mathilde Laigle was a French historian, governess to the governor of Iowa's children, "
                   "and an expert on Christine de Pizan. She is credited with helping to revive interest in the early"
                   " feminist movement.",
        "thumbnail": {
            "source": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Mathilde_Laigle_portrait_de_Gu%C3"
                      "%A9rin.jpg/320px-Mathilde_Laigle_portrait_de_Gu%C3%A9rin.jpg"
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

def test_main_fails_on_request_error(runner, mock_request_get):
    mock_request_get.side_effect = Exception('Boom')
    result = runner.invoke(console.main)
    assert result.exit_code == 1