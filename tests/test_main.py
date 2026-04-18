import pytest

def convert_to_positive(points):
    return [(abs(x), abs(y)) for x, y in points]

def test_convert_to_positive():
    points = [(-1, 2), (3, -4), (0, 0), (-5, -6)]
    expected_result = [(1, 2), (3, 4), (0, 0), (5, 6)]
    assert convert_to_positive(points) == expected_result

def test_convert_to_positive_empty_list():
    points = []
    expected_result = []
    assert convert_to_positive(points) == expected_result

def test_convert_to_positive_single_point():
    points = [(1, 2)]
    expected_result = [(1, 2)]
    assert convert_to_positive(points) == expected_result
