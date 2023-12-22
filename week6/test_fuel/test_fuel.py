import pytest
from fuel import convert, gauge

# testing convert() success cases
def test_convert_true():
    assert convert("3/4") == 75
    assert convert("1/3") == 33
    assert convert("2/3") == 67
    assert convert("0/10") == 0

# testing convert() failure or error cases
def test_convert_false():
    # ValueError case
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("5-10")
    with pytest.raises(ValueError):
        convert("1.5/10")
    with pytest.raises(ValueError):
        convert("5/1")

    # ZeroDivisionCase
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

# testing gauge() success case
def test_gauge_true():
    assert gauge(75) == "75%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"

# testing gauge() failure or error case
def test_gauge_false():
    # TypeError case
    with pytest.raises(TypeError):
        gauge("four")
    with pytest.raises(TypeError):
        gauge(None)
