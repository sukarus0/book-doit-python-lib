import textwrap

def test_textwrap_wrap():
    long_text = "Life is too short, you need python."*10

    result = textwrap.wrap(long_text, width=70)

    assert len(result) == 6


def test_textwrap_wrap_and_join():
    long_text = "Life is too short, you need python."*10

    result = textwrap.wrap(long_text, width=70)
    result = ' '.join(result)

    assert "Life is too short, you need python."*10 == result 
