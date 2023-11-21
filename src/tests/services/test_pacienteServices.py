import unittest
import requests

class TestApp(unittest.TestCase):
    URL = "http://127.0.0.1:5000/pacientes"
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer '}


    def test_get_users(self):
        """Get list of users"""
        response = requests.get(self.URL, headers=self.headers)
        if response.ok:
            return response
        else:
            return None

    def test_save_user(self):
        """save list of users"""
        response = requests.get(self.URL, headers=self.headers)
        if response.ok:
            return response
        else:
            return None

if __name__ == "__main__":
    tester = TestApp()