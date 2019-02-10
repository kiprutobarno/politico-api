from .base_test import *

class PartyTestCase(BaseTestCase):
    """ This class represents the party test cases and inherits from BaseTestCase class """
    
    def setUp(self):
        super().setUp()

    def test_create_party(self):
        """ Test that endpoint can create party """
        response = super().create_party(party)
        self.assertEqual(response.status_code, 201)
        response_content =  json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 201)

    def test_get_all_parties(self):
        """ Test that endpoint can retrieve all parties """
        super().create_party(party)
        response = super().get_all_parties()
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['message'] == "Success")

    def test_get_specific_party(self):
        """ Test that endpoint can retrieve a specific political party """
        super().create_party(party)
        response = super().get_specific_party()
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['message'] == "Success")

    def test_edit_party(self):
        """ Test that endpoint can update details of a specific party """
        super().create_party(party)
        response = super().edit_party(party_edit_data)
        response_content = json.loads(response.data.decode())
        self.assertEqual(response_content['message'], "Success")
        
    def test_delete_party(self):
        """ Test that endpoint can delete a specific party """
        super().create_party(party)
        response = super().delete_party()
        response_content = json.loads(response.data.decode())
        self.assertEqual(response_content['message'], "Success")

    def test_empty_party(self):
        """Test that endpoint cannot accept an empty party body"""
        response = super().create_party(empty_data_party)
        response_content =  json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    def test_blank_name(self):
        """Test that endpoint cannot accept a blank name"""
        response = super().create_party(party_blank_name)
        response_content =  json.loads(response.data.decode())
        self.assertTrue(response_content['message'] == 'name cannot be blank')

    def test_blank_hqAddress(self):
        """Test that endpoint cannot accept a blank hqAddress"""
        response = super().create_party(party_blank_hqAddress)
        response_content =  json.loads(response.data.decode())
        self.assertTrue(response_content['message'] == 'hqAddress cannot be blank')

    def test_blank_logoUrl(self):
        """Test that endpoint cannot accept a logoUrl"""
        response = super().create_party(party_blank_logoUrl)
        response_content =  json.loads(response.data.decode())
        self.assertTrue(response_content['message'] == 'logoUrl cannot be blank')
    

    def tearDown(self):
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()