# conftest.py is used to make the fixture global for other files

import pytest
import source.my_fixtures as my_fixtures

@pytest.fixture
def my_rectangle():
    return my_fixtures.Rectangle(10, 20)


@pytest.fixture
def weird_rectangle():
    return my_fixtures.Rectangle(5, 6)