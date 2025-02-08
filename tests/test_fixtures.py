# Using fixtures in testing


# import pytest
# import source.my_fixtures as my_fixtures


# @pytest.fixture
# def my_rectangle():
#     return my_fixtures.Rectangle(10, 20)


# @pytest.fixture
# def weird_rectangle():
#     return my_fixtures.Rectangle(5, 6)

# Now we're using conftest.py for globally accessing fixtures


def test_area(my_rectangle):
    result = my_rectangle.area()
    expected = 10 * 20
    assert result == expected


def test_perimeter(my_rectangle):
    result = my_rectangle.perimeter()
    expected = 2 * (10 + 20)
    assert result == expected


def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle


# Running Command: pytest test_fixtures.py