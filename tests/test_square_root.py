from src.square_root import square_root
import pytest

def test_positive_number():
    assert square_root(9) == 3

def test_zero():
    assert square_root(0) == 0

def test_negative_number():
    with pytest.raises(ValueError):
        square_root(-4)