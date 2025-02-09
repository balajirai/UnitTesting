

import unittest
import requests
import responses
from source.my_mocking4 import get_joke


class TestGetJoke(unittest.TestCase):


    @responses.activate
    def test_get_joke_returns_a_joke(self):
        responses.get(
            url = "http://api.icndb.com/jokes/random",
            json = {"value": {"joke": "Hello World"}},
            status = 200
        )

        self.assertEqual(get_joke(), "Hello World")


    @responses.activate
    def test_get_joke_raise_for_status(self):
        responses.get(
            url = "http://api.icndb.com/jokes/random",
            json = {"value": {"joke": "Hello World"}},
            status = 403
        )

        self.assertEqual(get_joke(), "HTTPError was raised")


    @responses.activate
    def test_get_joke_connection_error(self):
        responses.get(
            url = "http://api.icndb.com/jokes/random",
            body = requests.ConnectionError("ConnectionError was raised")
        )

        self.assertEqual(get_joke(), "ConnectionError was raised")

