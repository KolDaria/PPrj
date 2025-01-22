import pytest

from src.decorators import log, my_function


def test_log(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out in 'my_function ok'


def test_log_1():
    @log(filename=None)
    def my_function(x, y):
        return x + y
    my_function(1, 2)
    assert 3


def test_log_exception():
    with pytest.raises(Exception):
        my_function("1", 2)
