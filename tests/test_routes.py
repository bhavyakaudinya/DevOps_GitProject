import unittest
from app import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_invalid_method(self):
        response = self.client.post('/home')  
        self.assertEqual(response.status_code, 405)

if __name__ == '__main__':
    unittest.main()
