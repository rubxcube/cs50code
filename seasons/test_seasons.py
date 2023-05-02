from seasons import convert
import pytest



def test_date():
    assert convert("2021-12-27") == "Five hundred twenty-five thousand, six hundred minutes"


def test_birthdays():
    with pytest.raises(SystemExit):
        convert("December 27, 2021")
