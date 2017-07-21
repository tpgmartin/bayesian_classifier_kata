import pandas as pd

from nbc import trained, fprob

df = trained()


def test_good_is_nice():
    result = fprob('nice', 'good', df)
    assert result == 1.0


def test_john_is_fifty_fifty():
    result = fprob('nice', 'John', df)
    assert result == 0.5


def test_foo_is_zero():
    df = trained()
    result = fprob('nice', 'foo', df)
    assert result == 0.0
