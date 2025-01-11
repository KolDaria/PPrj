import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("state, expected", [
    ('CANCELED', [{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:19:33.419441'},
                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]),
    ('EXECUTED', [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                  {'id': 41428829, 'state': 'EXECUTED', 'date': '2017.07.03T18:35:29.512364'}]),
    ('DELETE', [])
])
def test_filter_by_state(coll, state, expected):
    assert filter_by_state(coll, state) == expected


def test_sort_by_date(coll):
    assert sort_by_date(coll) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:19:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2017.07.03T18:35:29.512364'}]
    assert sort_by_date(coll, False) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2017.07.03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:19:33.419441'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
