from collections import deque

def test_deque_rotate():
    a = "1 2 3 4 5"
    a = a.split()

    q = deque(a)
    q.rotate(2)

    result = list(q)

    assert result == '4 5 1 2 3'.split()
