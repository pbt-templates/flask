import os
import app
import unittest
import tempfile

class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def tearDown(self):
        pass

    def test_empty_db(self):
        response = self.app.get('/')
        # FIXME
        self.assertEqual(response.data, b'Hello World!!')

if __name__ == '__main__':
    unittest.main()
