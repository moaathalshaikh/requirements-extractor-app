from flask import Flask, jsonify, request
import unittest

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_extract_requirements(self):
        response = self.client.post('/extract', json={'text': 'Sample requirement text.'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('functional_requirements', response.json)
        self.assertIn('non_functional_requirements', response.json)

if __name__ == '__main__':
    unittest.main()