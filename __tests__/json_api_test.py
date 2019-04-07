import sys
import json
import unittest

sys.path.append('../..')
from api import *

class TestFunctions(unittest.TestCase):
    def setup(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        # Test of Output function
        
        def test_output(self):
            with app.test_request_context():
                out = output('true','cleartext', '1234','true', '[]')
            response = [
              {
                  'active': 'true',
                  'authentication_method': 'cleartext',
                  'password': '1234',
                  'authenticated': 'false',
                  'roles': '[]'
               }
            ]
            data = json.loads(out.get_data(as_text=True))
            # Assert response
            self.assertEqual(data['response'], response)

if __name__ == '__main__':
      unittest.main()