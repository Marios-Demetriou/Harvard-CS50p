from newTwttr import shorten

def test_str_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("testing") == "tstng"
    assert shorten("welcome") == "wlcm"
    assert shorten("what's up") == "wht's p"


def test_str_upper():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TESTING") == "TSTNG"
    assert shorten("WELCOME") == "WLCM"
    assert shorten("WHAT'S UP") == "WHT'S P"