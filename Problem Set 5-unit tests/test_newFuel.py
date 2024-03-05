import pytest

from newFuel import convert, gauge


def test_convert():
    assert convert("0/4") == 0
    assert convert("1/4") == 25
    assert convert("2/4") == 50
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    with pytest.raises(ValueError):
        convert("5/3")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("1/dog")
    with pytest.raises(ValueError):
        convert("dog/1")



def test_gauge():
    assert gauge(1) == "E"
    assert gauge(5) == "5%"
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

