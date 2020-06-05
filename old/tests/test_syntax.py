import pytest

import syntax


@pytest.mark.parametrize(
    "original, depth, expected",
    [
        ("after this we have {{{asdfasdf}}} and things", 0, "after this we have \"Hello world!\" and things"),
    ],
)
def test_resolution(original, depth, expected):
    text = "after this we have {{{asdfasdf}}} and things"
    new_text = syntax.resolve_embeddings(original)
    assert new_text == expected
