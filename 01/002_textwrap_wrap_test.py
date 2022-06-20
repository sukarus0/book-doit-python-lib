import textwrap
import pytest

@pytest.fixture
def long_text():
    text = "Life is too short, you need python. "*10

    return text


def test_textwrap_wrap(long_text):
    result = textwrap.wrap(long_text, width=70)

    assert len(result) == 6


def test_textwrap_wrap_and_join(long_text):
    result = textwrap.wrap(long_text, width=70)
    result = '\n'.join(result)

    assert result  == \
"""Life is too short, you need python. Life is too short, you need
python. Life is too short, you need python. Life is too short, you
need python. Life is too short, you need python. Life is too short,
you need python. Life is too short, you need python. Life is too
short, you need python. Life is too short, you need python. Life is
too short, you need python."""


def test_textwrap_fill(long_text):
    result = textwrap.fill(long_text, width=70)

    assert result  == \
"""Life is too short, you need python. Life is too short, you need
python. Life is too short, you need python. Life is too short, you
need python. Life is too short, you need python. Life is too short,
you need python. Life is too short, you need python. Life is too
short, you need python. Life is too short, you need python. Life is
too short, you need python."""
