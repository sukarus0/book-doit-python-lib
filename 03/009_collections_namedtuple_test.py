from collections import namedtuple
import pytest

@pytest.fixture
def data():
    data = [
            tuple("홍길동 23 01099990001".split()),
            tuple("김철수 31 01099991002".split()),
            tuple("이영희 23 01099992003".split())
        ]

    return data


@pytest.fixture
def Employee():
    Employee = namedtuple('Employee', 'name, age, cellphone')

    return Employee


def test_namedtuple_list_comprehension(data, Employee):

    data = [Employee(emp[0], emp[1], emp[2]) for emp in data]

    emp = data[0]

    assert emp.name == "홍길동"
    assert emp.age == "23"
    assert emp.cellphone == "01099990001"


def test_namedtuple_make(data, Employee):

    data = [Employee._make(emp) for emp in data]

    emp = data[0]

    assert emp.name == "홍길동"
    assert emp.age == "23"
    assert emp.cellphone == "01099990001"


def test_nametuple_asdict(data, Employee):

    data = [Employee._make(emp) for emp in data]

    emp = data[0]

    assert emp._asdict() == {'name': '홍길동', 'age' : '23', 'cellphone': '01099990001'}
