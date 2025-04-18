import pytest
import os
import time

@pytest.fixture
def file_setup_and_cleanup():
    nom = "data.test"
    f = open(nom, "wt")
    f.write("QUOI ?")
    f.close()
    print("End Set Up")
    time.sleep(5)

    yield nom

    print("Begin Clean Up")
    time.sleep(5)
    os.remove(nom)

def test_read_content(file_setup_and_cleanup):
    print(type(file_setup_and_cleanup))
    print(file_setup_and_cleanup)

    with open(file_setup_and_cleanup, "rt") as file:
        msg = file.readline()
        print(msg)
        assert msg == "QUOI ?"
