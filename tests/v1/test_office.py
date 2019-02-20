from .base_test import *
from app.api.v1.models.office import Office


class OfficeTestCase(BaseTestCase):
    """ This class represents the office test cases and "\
        " inherits from BaseTestCase class """

    # def test_create_office(self):
    #     """ Test that endpoint can create office"""
    #     response = super().create_office(office)
    #     self.assertEqual(response.status_code, 201)
    #     response_content = json.loads(response.data.decode())
    #     self.assertTrue(response_content['status'] == 201)

    def test_create_office_empty_name(self):
        """ Test that endpoint rejects blank name value """
        response = super().create_office(office_empty_name)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    def test_create_office_empty_type(self):
        """ Test that endpoint rejects blank type value """
        response = super().create_office(office_empty_type)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    def test_create_office_missing_name(self):
        """ Test that endpoint rejects bodies with missing key-pair values """
        response = super().create_office(office_missing_name_key)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    def test_non_string_name(self):
        """ Test that endpoint rejects non string name value """
        response = super().create_office(non_string_office_name)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    def test_non_string_type(self):
        """ Test that endpoint rejects non string type value """
        response = super().create_office(non_string_office_type)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    def test_empty_office(self):
        """ Test that endpoint rejects empty office body """
        response = super().create_office(office_empty_body)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    # def test_get_all_offices(self):
    #     """ Test that endpoint can retrieve all offices """
    #     super().create_office(office)
    #     response = super().get_all_offices()
    #     self.assertEqual(response.status_code, 200)
    #     response_content = json.loads(response.data.decode())
    #     self.assertTrue(response_content['message'] == "Success")

    # def test_get_specific_office(self):
    #     """ Test that endpoint can fetch specific political office """
    #     super().create_office(office)
    #     response = super().get_specific_office()
    #     self.assertEqual(response.status_code, 200)
    #     response_content = json.loads(response.data.decode())
    #     self.assertTrue(response_content['message'] == "Success")

    def test_nonexistent_offices(self):
        """ Test that endpoint will not accept retrieving non existent offices """
        Office().offices.clear()
        response = super().get_all_offices()
        response_content = json.loads(response.data.decode())
        self.assertTrue(
            response_content['message'] == "Sorry, no government office is currently available, try again later")

    def test_nonexistent_office(self):
        """ Test that endpoint will not accept retrieving non existent office """
        Office().offices.clear()
        response = super().get_specific_office()
        response_content = json.loads(response.data.decode())
        self.assertTrue(
            response_content['message'] == "Sorry, no such office exists, try again later!")


if __name__ == "__main__":
    unittest.main()
