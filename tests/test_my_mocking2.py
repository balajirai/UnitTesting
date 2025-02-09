# Using mocking (patch) in unit testing


import unittest
from unittest.mock import patch, MagicMock
from source.my_mocking2 import len_joke, get_joke


class TestJoke(unittest.TestCase):


    @patch("source.my_mocking2.get_joke")
    def test_len_joke(self, mock_len_joke):
        mock_len_joke.return_value = "one"
        self.assertEqual(len_joke(), 3)


    @patch("source.my_mocking2.requests")
    def test_get_joke(self, mock_requests):

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"value": {"joke": "Hello World"}}

        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(), "Hello World")



if __name__ == "__main__":
    unittest.main()