from .base_test import *
from .helper_data import *
from .helper_methods import *

class PartyTestCase(BaseTestCase):
    """ This class represents the party test case and inherits from BaseTestCase class """
    
    def setUp(self):
        super(PartyTestCase, self).setUp()

    def test_create_party(self):
        """ Test that endpoint can create party """
        response = create_party(self, party)
        self.assertEqual(response.status_code, 201)
        response_content =  json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 201)

    def test_get_all_parties(self):
        """ Test that endpoint can retrieve all parties """
        create_party(self, party)
        response = get_all_parties(self)
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['message'] == "Success")

    def test_get_specific_party(self):
        """ Test that endpoint can retrieve a specific political party """
        create_party(self, party)
        response = get_specific_party(self)
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['message'] == "Success")

    def test_edit_party(self):
        """ Test that endpoint can update details of a specific party """
        create_party(self, party)
        response = edit_party(self, party_edit_data)
        response_content = json.loads(response.data.decode())
        self.assertEqual(response_content['message'], "Success")
        
    def test_delete_party(self):
        """ Test that endpoint can delete a specific party """
        create_party(self, party)
        response = delete_party(self)
        response_content = json.loads(response.data.decode())
        self.assertEqual(response_content['message'], "Success")

if __name__ == "__main__":
    unittest.main()