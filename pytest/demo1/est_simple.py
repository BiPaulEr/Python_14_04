import pytest

def test_simple():
    assert 1 + 1 == 2 
    assert 2 in [1, 2, 3]
    assert isinstance("", str)
    with pytest.raises( (ValueError, ZeroDivisionError) ):
        2 / 0
    chaine = "OK"
    assert "O" in chaine

@pytest.fixture(scope="session")
def prepare_list_session():
    print("PREPARE LIST FOR SESSION")
    return [1, 2]

def test_sum_session(prepare_list_session):
    assert sum(prepare_list_session) == 3

@pytest.fixture(scope="module")
def prepare_list():
    print("PREPARE LIST")
    return [1, 2, 3, 4]

def test_sum(prepare_list):
    assert sum(prepare_list) == 10
    prepare_list.append(9999999)

def test_len(prepare_list):
    assert len(prepare_list) == 5

@pytest.fixture(scope="class")
def prepare_data_for_class():
    print("prepare_data_for_class")
    return "classe"

class TestClass:
    def test_class_1(self, prepare_data_for_class):
        assert prepare_data_for_class == "classe"
    def test_class_2(self, prepare_data_for_class):
        assert prepare_data_for_class == "classe"

class TestClass2:
    def test_class_1(self, prepare_data_for_class):
        assert prepare_data_for_class == "classe"
    def test_class_2(self, prepare_data_for_class):
        assert prepare_data_for_class == "classe"