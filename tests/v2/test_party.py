from .base_test import *

class PartyTestCase(BaseTestCase):
    """ This class represents the party test cases and inherits from BaseTestCase class """
    
    def setUp(self):
        super().setUp()

    def test_create_party(self):
        """ Test that endpoint can create party """
        super().create_user(admin_user)
        login=super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token=[d['token'] for d in login_content['data']][0]
        response = super().create_party(party, token)
        response_content =  json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 201)

    def test_empty_party(self):
        """Test that endpoint cannot accept an empty party body"""
        super().create_user(admin_user)
        login=super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token=[d['token'] for d in login_content['data']][0]
        response = super().create_party(empty_data_party, token)
        response_content =  json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    def test_blank_name(self):
        """Test that endpoint cannot accept a blank name"""
        super().create_user(admin_user)
        login=super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token=[d['token'] for d in login_content['data']][0]
        response = super().create_party(party_blank_name, token)
        response_content =  json.loads(response.data.decode())
        self.assertTrue(response_content['message'] == 'name cannot be blank')

    def test_blank_hqAddress(self):
        """Test that endpoint cannot accept a blank hqAddress"""
        super().create_user(admin_user)
        login=super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token=[d['token'] for d in login_content['data']][0]
        response = super().create_party(party_blank_hqAddress, token)
        response_content =  json.loads(response.data.decode())
        self.assertTrue(response_content['message'] == 'hqAddress cannot be blank')

    def test_blank_logoUrl(self):
        """Test that endpoint cannot accept a logoUrl"""
        super().create_user(admin_user)
        login=super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token=[d['token'] for d in login_content['data']][0]
        response = super().create_party(party_blank_logoUrl, token)
        response_content =  json.loads(response.data.decode())
        self.assertTrue(response_content['message'] == 'logoUrl cannot be blank')

    def test_non_string_name(self):
        """Test that endpoint cannot accept non string name"""
        super().create_user(admin_user)
        login=super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token=[d['token'] for d in login_content['data']][0]
        response = super().create_party(party_non_string_name, token)
        response_content =  json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    def test_non_string_hqAddress(self):
        """Test that endpoint cannot accept non string hqAddress"""
        super().create_user(admin_user)
        login=super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token=[d['token'] for d in login_content['data']][0]
        response = super().create_party(party_non_string_hqAddress, token)
        response_content =  json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    def test_get_all_parties(self):
        """ Test that endpoint can retrieve all parties """
        super().create_user(admin_user)
        login=super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token=[d['token'] for d in login_content['data']][0]
        response = super().get_all_parties(token)
        response_content = json.loads(response.data.decode())
        print(response_content)
        self.assertTrue(response_content['message'] == "Success")

    def test_get_specific_party(self):
        """ Test that endpoint can retrieve a specific political party """
        super().create_user(admin_user)
        login=super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token=[d['token'] for d in login_content['data']][0]
        response = super().get_specific_party(token)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 200)


    def tearDown(self):
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()