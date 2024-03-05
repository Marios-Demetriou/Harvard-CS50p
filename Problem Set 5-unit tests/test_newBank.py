from newBank import value

def test_zero_price():
    assert value("hello") == "$0"
    assert value("Hello") == "$0"


def test_twenty_price():
    assert value("hi") == "$20"
    assert value("help") == "$20"
    assert value("Home") == "$20"


def test_hundred_price():
    assert value("bank") == "$100"
    assert value("Welcome") == "$100"
    assert value("space") == "$100"

