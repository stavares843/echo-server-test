import unittest
import requests

class TestEchoServer(unittest.TestCase):
    BASE_URL = 'http://localhost:8080'

    def test_get_request(self):
        response = requests.get(f'{self.BASE_URL}/test-get')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Received GET request:', response.text)

    def test_post_request(self):
        response = requests.post(f'{self.BASE_URL}/test-post', data='Test data')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Received POST request:', response.text)
        self.assertIn('Body:', response.text)

if __name__ == '__main__':
    unittest.main()
