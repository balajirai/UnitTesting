# pytest mark (slow or skip) testing


import time
import pytest
import source.my_mark_skip as my_mark


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_mark.add(1, 4)
    assert result == 5


@pytest.mark.skip(reason="This feature is currently broken")
def test_skip():
    result = my_mark.add(1, 4)
    assert result == 5


@pytest.mark.xfail(reason="We know we cannot divide by zero")
def test_divide_zero_broken():
    my_mark.divide(4, 0)



# Running Command: pytest test_my_mark_skip.py
# Running Command: pytest -m slow (we're just selecting one of the mark here slow)