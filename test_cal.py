import cal
import pytest


def test_do_cal():
    assert cal.do_cal(2) == 4
    assert cal.do_cal(3) == 9
    assert cal.do_cal(4) == 16

