# Class based testing

import math
import pytest
import source.my_class as my_class


class TestCircle:


    def setup_method(self, method):
        print(f"Setting up the {method}")
        self.circle = my_class.Circle(10)


    def teardown_method(self, method):
        print(f"Tearing down the {method}")
        del self.circle


    def test_area(self):
        result = self.circle.area()
        expected = math.pi * self.circle.radius ** 2
        assert result == expected


    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected


# Running Command: pytest test_my_class.py