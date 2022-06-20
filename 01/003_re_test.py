import pytest
import re

@pytest.fixture
def data():
    data = """
홍길동의 주민등록번호는 800905-1049118 입니다.
그리고 고길동의 주민등록번호는 700905-1059119 입니다.
그렇다면 누가 형님일까요?
"""

    return data


def test_substitute(data):
    pat = re.compile("(\d{6})[-]\d{7}")
    result = pat.sub("\g<1>-*******", data)

    assert result == """
홍길동의 주민등록번호는 800905-******* 입니다.
그리고 고길동의 주민등록번호는 700905-******* 입니다.
그렇다면 누가 형님일까요?
"""
