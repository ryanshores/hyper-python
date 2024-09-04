import pytest


@pytest.fixture
def mock_requests_get(mocker):
    mock = mocker.patch("requests.get")
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
