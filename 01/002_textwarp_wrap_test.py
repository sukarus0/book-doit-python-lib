import textwrap

def test_textwrap_wrap():
    long_text = "Life is too short, you need python."*10

    result = textwrap.wrap(long_text, width=70)

    assert len(result) == 6
