from .base_test import *

class OfficeTestCase(BaseTestCase):
    """ This class represents the office test cases and inherits from BaseTestCase class """
    
    def setUp(self):
        super().setUp()

    def test_create_office(self):
        """ Test that endpoint can office party """
        response = super().create_office(office)
        self.assertEqual(response.status_code, 201)
        response_content =  json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 201)

    def test_get_all_offices(self):
        """ Test that endpoint can retrieve all offices """
        super().create_office(office)
        response = super().get_all_offices()
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['message'] == "Success")

    def test_get_specific_office(self):
        """ Test that endpoint can fetch a specific political office """
        super().create_office(office)
        response = super().get_specific_office()
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['message'] == "Success")

    def tearDown(self):
        return super().tearDown()
        
if __name__ == "__main__":
    unittest.main()