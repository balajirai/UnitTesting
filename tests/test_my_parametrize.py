# Using parametrizing in testing


import pytest
import source.my_parametrize as my_parametrize


@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (4, 16), (9, 81)])
def test_multiple_square_areas(side_length, expected_area):
    result = my_parametrize.Square(side_length).area()
    assert result == expected_area


@pytest.mark.parametrize("side_length, expected_perimeter", [(5, 20), (4, 16), (9, 36)])
def test_multiple_square_perimeters(side_length, expected_perimeter):
    result = my_parametrize.Square(side_length).perimeter()
    assert result == expected_perimeter


# Running Command: pytest test_my_parametrize.py