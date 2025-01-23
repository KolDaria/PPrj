import os

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


def test_logging_decorator():
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    with open("mylog.txt", "r") as file:
        log_content = file.read()
        assert "my_function ok" in log_content
    os.remove("mylog.txt")


def test_logging_decorator_exception():
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        my_function(1, 0)
    with open("mylog.txt", "r") as file:
        log_content = file.read()
        assert "my_function error" in log_content
    os.remove("mylog.txt")
