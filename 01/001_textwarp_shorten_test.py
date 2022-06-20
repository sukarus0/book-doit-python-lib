import textwrap

def test_textwrap_shorten_basic():
    text = "Life is too short, you need python."

    result = textwrap.shorten(text, width=15)

    assert result == "Life is [...]"


def test_textwrap_shorten_with_placeholder():
    text = "Life is too short, you need python."

    result = textwrap.shorten(text, width=15, placeholder=" *****")

    assert result == "Life is *****"

