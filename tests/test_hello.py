import pytest
import jonhello as jh

def test_greet():
    assert jh.greet() == 'hello, new file!'