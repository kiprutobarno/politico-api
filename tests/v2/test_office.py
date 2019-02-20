from .base_test import *


class OfficeTestCase(BaseTestCase):
    """ This class represents the party test cases and inherits from BaseTestCase class """

    # def setUp(self):
    #     super().setUp()

    def test_create_office(self):
        """ Test that endpoint can create office"""
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        response = super().create_office(office, token)
        self.assertEqual(response.status_code, 201)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 201)

    def test_create_office_empty_name(self):
        """ Test that endpoint rejects blank name value """
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        response = super().create_office(office_empty_name, token)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    def test_create_office_empty_type(self):
        """ Test that endpoint rejects blank type value """
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        response = super().create_office(office_empty_type, token)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    def test_create_office_missing_name(self):
        """ Test that endpoint rejects bodies with missing key-pair values """
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        response = super().create_office(office_missing_name_key, token)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    def test_non_string_name(self):
        """ Test that endpoint rejects non string name value """
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        response = super().create_office(non_string_office_name, token)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    def test_non_string_type(self):
        """ Test that endpoint rejects non string type value """
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        response = super().create_office(non_string_office_type, token)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    def test_empty_office(self):
        """ Test that endpoint rejects empty office body """
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        response = super().create_office(office_empty_body, token)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    def test_get_all_offices(self):
        """ Test that endpoint can retrieve all offices """
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        super().create_office(office, token)
        response = super().get_all_offices(token)
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 200)

    def test_get_specific_office(self):
        """ Test that endpoint can fetch specific political office """
        super().create_user(admin_user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        super().create_office(office, token)
        response = super().get_specific_office(token)
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 200)

    def test_get_nonexistent_offices(self):
        """ Test that endpoint will not accept retrieving non existent offices """
        super().create_user(admin_user)
        login=super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token=[d['token'] for d in login_content['data']][0]
        response = super().get_all_offices(token)
        self.assertEqual(response.status_code, 404)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 404)

    
    def test_get_nonexistent_office(self):
        """ Test that endpoint will not accept retrieving non existent offices """
        super().create_user(admin_user)
        login=super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token=[d['token'] for d in login_content['data']][0]
        response = super().get_specific_office(token)
        self.assertEqual(response.status_code, 404)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 404)
