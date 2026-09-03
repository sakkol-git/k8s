import unittest
import json
from main import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True 

    def test_hello_endpoint(self):
        # Send a GET request to the root '/'
        response = self.app.get('/')
        
        # Check the status code
        self.assertEqual(response.status_code, 200)
        
        # Check the response data
        data = json.loads(response.data)
        self.assertEqual(data['message'], "Hello from Flask!")

if __name__ == '__main__':
    unittest.main()
