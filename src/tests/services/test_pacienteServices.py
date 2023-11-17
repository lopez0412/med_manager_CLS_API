import unittest
import requests

class TestApp(unittest.TestCase):
    URL = "http://127.0.0.1:5000/pacientes"
    TEST_TOKEN = ""

    def test_get_users():
        """Get list of users"""
        response = requests.get(URL)
        if response.ok:
            return response
        else:
            return None

if __name__ == "__main__":
    tester = TestApp()