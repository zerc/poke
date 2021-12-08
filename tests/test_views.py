import pytest

from app import app
from providers.pokeapi import Pokemon


@pytest.fixture
def client():
    app.config.update({"TESTING": True})

    with app.test_client() as client:
        yield client


def test_get_pokemon(client, mocker):
    mocker.patch(
        "providers.pokeapi.get_pokemon",
        return_value=Pokemon(
            name="mewtwo", description="bla-bla", habitat="rare", isLegendary=True
        ),
    )

    response = client.get("/pokemon/mewtwo")
    assert response.status_code == 200
    assert response.json == {
        "name": "mewtwo",
        "description": "bla-bla",
        "habitat": "rare",
        "isLegendary": True,
    }
