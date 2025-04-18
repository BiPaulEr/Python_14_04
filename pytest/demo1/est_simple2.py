import pytest
from test_simple import prepare_list, prepare_list_session

def test_len_simple_2(prepare_list):
    assert len(prepare_list) == 4

def test_sum_session(prepare_list_session):
    assert sum(prepare_list_session) == 3