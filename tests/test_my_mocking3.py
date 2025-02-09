# Using mocking (patch) in unit testing


import unittest
import requests.exceptions
from unittest.mock import patch, MagicMock
from source.my_mocking3 import len_joke, get_joke
from requests.exceptions import Timeout, HTTPError


class TestJoke(unittest.TestCase):


    @patch("source.my_mocking3.get_joke")
    def test_len_joke(self, mock_len_joke):
        mock_len_joke.return_value = "one"
        self.assertEqual(len_joke(), 3)


    @patch("source.my_mocking3.requests")
    def test_get_joke(self, mock_requests):

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"value": {"joke": "Hello World"}}

        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(), "Hello World")


    @patch("source.my_mocking3.requests")
    def test_fail_get_joke(self, mock_requests):

        mock_response = MagicMock()
        mock_response.status_code = 403
        mock_response.json.return_value = {"value": {"joke": "Hello World"}}

        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(), "No jokes")


    @patch("source.my_mocking3.requests")
    def test_get_joke_timout_exception(self, mock_requests):

        mock_requests.exceptions = requests.exceptions
        mock_requests.get.side_effect = Timeout("Seems that the server is down")

        self.assertEqual(get_joke(), "No jokes")


    @patch("source.my_mocking3.requests")
    def test_get_joke_raise_for_status(self, mock_requests):

        mock_requests.exceptions = requests.exceptions
        mock_response = MagicMock()
        mock_response.status_code = 403
        mock_response.raise_for_status.side_effect = HTTPError("Something went wrong")
        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(), "HTTPError was raised")    # self.assertRaises(HTTPError, get_joke)



if __name__ == "__main__":
    unittest.main()