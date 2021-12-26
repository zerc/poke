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


@pytest.mark.parametrize(
    ["habitat", "is_legendary", "expected_description"],
    [
        ("cave", False, "Force be with you"),
        ("rare", True, "Force be with you"),
        ("cave", True, "Force be with you"),
        ("rare", False, "Valorous morrow to thee"),
        (None, False, "Valorous morrow to thee"),
    ],
)
def test_get_pokemon_translated(
    client, mocker, habitat, is_legendary, expected_description
):
    mocker.patch(
        "providers.pokeapi.get_pokemon",
        return_value=Pokemon(
            name="mewtwo",
            description="bla-bla",
            habitat=habitat,
            isLegendary=is_legendary,
        ),
    )

    mocker.patch("providers.funtransapi.as_yoda", return_value="Force be with you")
    mocker.patch(
        "providers.funtransapi.as_shakespeare", return_value="Valorous morrow to thee"
    )
    response = client.get("/pokemon/translated/mewtwo")
    assert response.status_code == 200
    assert response.json == {
        "name": "mewtwo",
        "description": expected_description,
        "habitat": habitat,
        "isLegendary": is_legendary,
    }
