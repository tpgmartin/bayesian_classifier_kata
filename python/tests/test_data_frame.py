import pandas as pd

from nbc import trained


def test_data_frame_exists():
    result = trained()
    assert isinstance(result, pd.DataFrame)
