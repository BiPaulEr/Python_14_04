import pytest
import sys

@pytest.mark.skip
@pytest.mark.unit
def test_simple_unit():
    print("test_simple_unit")
    assert True

@pytest.mark.skipif("sys.platform == 'win32'", reason="Test que sur linux")
@pytest.mark.unit
def test_linux_unit():
    print("test_linux_unit")
    print(sys.platform)
    assert sys.platform != "win32"

@pytest.mark.xfail
@pytest.mark.unit
def test_xfail():
    assert 1 == 0

@pytest.mark.unit
def test_simple_2_unit():
    print("test_simple_2_unit")
    assert True

@pytest.mark.integration
def test_simple_integration():
    print("test_simple_integration")
    assert True

@pytest.mark.integration
def test_simple_2_integration():
    print("test_simple_2_integration")
    assert True

