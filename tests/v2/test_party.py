from .base_test import *


class PartyTestCase(BaseTestCase):
    """ This class represents the party test cases and inherits from BaseTestCase class """

    def test_create_party(self):
        """ Test that endpoint can create party """
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        response = super().create_party(party, token)
        response_content = json.loads(response.data.decode())
        self.assertEqual(response_content['status'], 201)

    def test_create_existing_party(self):
        """ Test that endpoint can create party """
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        super().create_party(party, token)
        response = super().create_party(party, token)
        response_content = json.loads(response.data.decode())
        self.assertEqual(
            response_content['message'], "Such a party is already registered!")

    def test_empty_party(self):
        """Test that endpoint cannot accept an empty party body"""
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        response = super().create_party(empty_data_party, token)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    def test_blank_name(self):
        """Test that endpoint cannot accept a blank name"""
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        response = super().create_party(party_blank_name, token)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['message'] == 'name cannot be blank')

    def test_blank_hqAddress(self):
        """Test that endpoint cannot accept a blank hqAddress"""
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        response = super().create_party(party_blank_hqAddress, token)
        response_content = json.loads(response.data.decode())
        self.assertTrue(
            response_content['message'] == 'hqAddress cannot be blank')

    def test_blank_logoUrl(self):
        """Test that endpoint cannot accept a logoUrl"""
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        response = super().create_party(party_blank_logoUrl, token)
        response_content = json.loads(response.data.decode())
        self.assertTrue(
            response_content['message'] == 'logoUrl cannot be blank')

    def test_invalid_logoUrl(self):
        """Test that endpoint cannot accept a logoUrl"""
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        response = super().create_party(party_invalid_logoUrl, token)
        response_content = json.loads(response.data.decode())
        self.assertEqual(
            response_content['message'], 'Invalid logo url')

    def test_non_string_name(self):
        """Test that endpoint cannot accept non string name"""
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        response = super().create_party(party_non_string_name, token)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    def test_non_string_hqAddress(self):
        """Test that endpoint cannot accept non string hqAddress"""
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        response = super().create_party(party_non_string_hqAddress, token)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    def test_get_all_parties(self):
        """ Test that endpoint can retrieve all parties """
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        super().create_party(party, token)
        response = super().get_all_parties(token)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 200)

    def test_get_nonexisting_parties(self):
        """ Test that endpoint can retrieve all parties """
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        response = super().get_all_parties(token)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['message']
                        == "No party is currently registered")

    def test_get_specific_party(self):
        """ Test that endpoint can retrieve a specific political party """
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        super().create_party(party, token)
        response = super().get_specific_party(token)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['message'] == "Success")

    def test_get_specific_party_invalid(self):
        """ Test that endpoint can retrieve a specific political party """
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        super().create_party(party, token)
        response = super().get_specific_party_invalid(token)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['message']
                        == "Unacceptable id format")

    def test_delete_party(self):
        """ Test that endpoint can create party """
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        super().create_party(party, token)
        response = super().delete_party(token)
        response_content = json.loads(response.data.decode())
        self.assertEqual(
            response_content['message'], "Party successfully deleted!")

    def test_delete_non_existent(self):
        """Test endpoint will not accept a zero and an id"""
        super().create_user(admin_user)
        login=super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token=[d['token'] for d in login_content['data']][0]
        response = super().delete_party(token)
        response_content = json.loads(response.data.decode())
        self.assertEqual(response_content['message'], "You cannot delete a non-existent party")
        self.assertEqual(response_content['status'], 404)

    def test_delete_invalid_id(self):
        """Test endpoint will not accept a zero and an id"""
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        response = super().invalid_delete_party(token)
        response_content = json.loads(response.data.decode())
        self.assertEqual(response_content['message'], 'Unacceptable id format')

    def test_edit_party(self):
        """ Test that endpoint can update details of a specific party """
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        super().create_party(party, token)
        response = super().edit_party(party_edit_data, token)
        response_content = json.loads(response.data.decode())
        self.assertEqual(
            response_content['message'], "Party details successfully updated!")

    def test_edit_party_invalid_logo(self):
        """ Test that endpoint can update details of a specific party """
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        response = super().edit_party(party_edit_invalid_logo, token)
        response_content = json.loads(response.data.decode())
        self.assertEqual(
            response_content['message'], "Invalid logo url")

    def test_edit_party_invalid(self):
        """ Test that endpoint can update details of a specific party """
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        response = super().edit_party_invalid(party_edit_data, token)
        response_content = json.loads(response.data.decode())
        self.assertEqual(
            response_content['message'], "Unacceptable id format")

    def test_edit_without_name(self):
        """ Test that endpoint can update details of a specific party """
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        response = super().edit_party(party_missing_name_key, token)
        response_content = json.loads(response.data.decode())
        self.assertEqual(response_content['message'], "name key missing")


    def test_edit_non_existing(self):
        """ Test that endpoint can update details of a specific party """
        super().create_user(admin_user)
        login=super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token=[d['token'] for d in login_content['data']][0]
        response = super().edit_party(party_edit_data, token)
        response_content = json.loads(response.data.decode())
        self.assertEqual(response_content['message'], "You cannot edit a non-existent party")


    def test_edit_blank_name(self):
        """Test that endpoint cannot accept a blank name"""
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        response = super().edit_party(party_blank_name, token)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    def test_edit_blank_hqAddress(self):
        """Test that endpoint cannot accept a blank hqAddress"""
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        response = super().edit_party(party_blank_hqAddress, token)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    def test_edit_blank_logoUrl(self):
        """Test that endpoint cannot accept a non existing logoUrl"""
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        response = super().edit_party(party_blank_logoUrl, token)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    def test_edit_non_string_name(self):
        """Test that endpoint cannot accept non string name"""
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        response = super().edit_party(party_non_string_name, token)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    def test_edit_non_string_hqAddress(self):
        """Test that endpoint cannot accept non string hqAddress"""
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        response = super().edit_party(party_non_string_hqAddress, token)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

if __name__ == "__main__":
    unittest.main()
