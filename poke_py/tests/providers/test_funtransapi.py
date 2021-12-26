import pytest
import responses

from providers import funtransapi


@responses.activate
@pytest.mark.parametrize(
    ["translation_type", "expected_output"],
    [
        ("yoda", "Force be with you world"),
        ("shakespeare", "Valorous morrow to thee,  sir ordinary"),
    ],
)
def test_translation(translation_type: str, expected_output: str):
    with open(f"tests/mocks/{translation_type}.json", "r") as f:
        responses.add(
            responses.POST,
            f"https://api.funtranslations.com/translate/{translation_type}.json",
            body=f.read(),
        )

    try:
        func = getattr(funtransapi, f"as_{translation_type}")
    except AttributeError:
        raise AttributeError(
            "New translation types expected to a function named as follow: as_<translation_type>"
        )

    assert func("hello world") == expected_output
