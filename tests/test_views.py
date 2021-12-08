import pytest

from app import app


@pytest.fixture
def client():
    app.config.update({"TESTING": True})

    with app.test_client() as client:
        yield client


def test_get_pokemon(client):
    response = client.get("/pokemon/mewtwo")
    assert response.status_code == 200
    assert response.json == {
        "name": "mewtwo",
        "description": (
            "It was created by a scientist after years of horrific genesplicing and DNA engineering experiments."
        ),
        "habitat": "rare",
        "isLegendary": True,
    }
