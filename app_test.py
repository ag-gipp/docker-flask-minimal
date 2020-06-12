import unittest

import app


class BasicTest(unittest.TestCase):
    def testMainPage(self):
        client = app.app.test_client()
        client.testing = True
        response = client.get('/')
        self.assertEqual(200, response.status_code)
        self.assertIn(b'Demo Python', response.data)
