import responses

from providers.pokeapi import get_pokemon


@responses.activate
def test_get_pokemon():
    with open("tests/mocks/wormadam.json", "r") as f:
        responses.add(
            responses.GET,
            "https://pokeapi.co/api/v2/pokemon-species/wormadam/",
            body=f.read(),
        )

    pokemon = get_pokemon("wormadam")
    assert pokemon.name == "wormadam"
    assert (
        pokemon.description
        == "When BURMY evolved, its cloak\nbecame a part of this Pokémon’s\nbody. The cloak is never shed."
    )
    assert pokemon.habitat == ""
    assert pokemon.isLegendary is False
