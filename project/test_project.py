from project import get_deposit, get_line, get_bet
import pytest


def test_get_deposit():
    with pytest.raises(SystemExit):
        get_deposit("abc")
    assert get_deposit(1000) == 1000
    assert get_deposit(555) == 555


def test_get_line():
    with pytest.raises(SystemExit):
        get_line("hundred")
    assert get_line(2) == 2
    assert get_line(1) == 1


def test_get_bet():
    MIN_BET = 10
    MAX_BET = 100
    with pytest.raises(SystemExit):
        get_bet("dollars")
    assert get_bet(50) == 50
    assert get_bet(100) == 100
