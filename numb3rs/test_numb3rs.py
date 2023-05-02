from numb3rs import validate


def test_second():
    assert validate("0.cat.123.4") == False

def test_range():
    assert validate("280.290.0.300") == False

def test_format():
    assert validate("123") == False

def test_first():
    assert validate("5.260.260.260") == False
