from newPlates import is_valid


def test_begin_char():  # Check for the 2 beginning characters:
    assert is_valid("CS50")
    assert is_valid("AAAA50")
    assert is_valid("AB")
    assert not is_valid("A1234")
    assert not is_valid("A123456")
    assert not is_valid("1ABC")
    assert not is_valid("12ABC")


def test_max_char():  # Check for length of input:
    assert is_valid("ABC123")
    assert is_valid("AB")
    assert not is_valid("OUTATIME")
    assert not is_valid("MAXLENGTH")
    assert not is_valid("A")


def test_in_middle():  # Check for numbers between letters:
    assert is_valid("CS50")
    assert not is_valid("CS50P")
    assert not is_valid("AB1C")
    assert not is_valid("AB5C6")


def test_zero_char():  # Check for zero as first number:
    assert not is_valid("CS012")
    assert not is_valid("CS0A")
    assert is_valid("CS102")
    assert is_valid("AB100")
    assert not is_valid("0ABC")


def test_special_char():  # Check for special characters
    assert is_valid("ABC123")
    assert not is_valid("A:B123")
    assert not is_valid("A#B^13")
    assert not is_valid("A#B1_3")
    assert not is_valid("{AB123")
    assert not is_valid("AB^12*")
    assert not is_valid("CS_*^%")

