from .base_test import *
from .helper_data import *
from .helper_methods import *

class OfficeTestCase(BaseTestCase):
    """ This class represents the party test case and inherits from BaseTestCase class """
    
    def setUp(self):
        super(OfficeTestCase, self).setUp()

    def test_create_office(self):
        """ Test that endpoint can office party """
        response = create_office(self, office)
        self.assertEqual(response.status_code, 201)
        response_content =  json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 201)


if __name__ == "__main__":
    unittest.main()