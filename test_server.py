import unittest
import threading
import requests
from http.server import HTTPServer
from echo_server import EchoHTTPRequestHandler

HOST, PORT = "localhost", 8080

class TestEchoHTTPRequestHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the server in a separate thread
        cls.server = HTTPServer((HOST, PORT), EchoHTTPRequestHandler)
        cls.thread = threading.Thread(target=cls.server.serve_forever)
        cls.thread.daemon = True  # added this to ensure server stops when test ends
        cls.thread.start()
    
    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()
    
    def test_get_request(self):
        # send GET request
        response = requests.get(f"http://{HOST}:{PORT}/test-path")
        
        # check status code
        self.assertEqual(response.status_code, 200)
        
        # check path and headers are echoed in the response body
        self.assertIn("Received GET request:", response.text)
        self.assertIn("Path: /test-path", response.text)
        self.assertIn("Headers:", response.text)
    
    def test_post_request(self):
        # POST request data
        data = {"key": "value"}
        
        # send POST request
        response = requests.post(f"http://{HOST}:{PORT}/test-path", data=data)
        
        # check status code
        self.assertEqual(response.status_code, 200)
        
        # check the path, headers, and body are echoed in the response body
        self.assertIn("Received POST request:", response.text)
        self.assertIn("Path: /test-path", response.text)
        self.assertIn("Headers:", response.text)
        self.assertIn("Body:", response.text)
        self.assertIn("key=value", response.text)

if __name__ == "__main__":
    unittest.main()
