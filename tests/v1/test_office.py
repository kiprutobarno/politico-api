from .base_test import *
from .helper_methods import *
from utils.helper_data import *

class OfficeTestCase(BaseTestCase):
    """ This class represents the office test cases and inherits from BaseTestCase class """
    
    def setUp(self):
        super(OfficeTestCase, self).setUp()

    def test_create_office(self):
        """ Test that endpoint can office party """
        response = create_office(self, office)
        self.assertEqual(response.status_code, 201)
        response_content =  json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 201)

    def test_get_all_offices(self):
        """ Test that endpoint can retrieve all offices """
        create_office(self, office)
        response = get_all_offices(self)
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['message'] == "Success")

    def test_get_specific_office(self):
        """ Test that endpoint can fetch a specific political office """
        create_office(self, office)
        response = get_specific_office(self)
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['message'] == "Success")

if __name__ == "__main__":
    unittest.main()