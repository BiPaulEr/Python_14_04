import pytest

liste = [1, 2, 3]
@pytest.fixture(params=liste)
def simple_fixtures(request):
    return request.param

@pytest.fixture(params=["A", "B", "C"])
def simple_fixtures_2(request):
    return request.param

def test_simple(simple_fixtures):
    print(simple_fixtures)
    assert True

def test_simple_2(simple_fixtures_2):
    print(simple_fixtures_2)
    assert True

def test_combi(simple_fixtures_2, simple_fixtures):
    print(simple_fixtures_2, " ->", simple_fixtures)
    assert True