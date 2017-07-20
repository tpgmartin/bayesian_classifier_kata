import pandas as pd

from nbc import trained, fprob


def test_good_is_nice():
    df = trained()
    result = fprob('nice', 'good', df)
    assert result == 1.0


def test_john_is_fifty_fifty():
    df = trained()
    result = fprob('nice', 'John', df)
    assert result == 0.5