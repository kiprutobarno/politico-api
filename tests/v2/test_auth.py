from .base_test import *


class UserTestCase(BaseTestCase):
    """ This class represents the user test cases and inherits from BaseTestCase class """

    # def setUp(self):
    #     super().setUp()

    def test_create_user(self):
        """ Test that endpoint can create user"""
        response = super().create_user(admin_user)
        self.assertEqual(response.status_code, 201)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 201)

    def test_user_login(self):
        """Test that endpoint can login a registered user"""
        super().create_user(admin_user)
        response = super().login_user(admin_user_login)
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 200)

    def test_wrong_password_login(self):
        """Test that endpoint cannot login a user using wrong password"""
        super().create_user(admin_user)
        response = super().login_user(wrong_password_login)
        self.assertEqual(response.status_code, 401)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['message'] == 'wrong credentials')

    def test_blank_email_login(self):
        """Test that endpoint cannot login a user using blank email"""
        super().create_user(admin_user)
        response = super().login_user(blank_email_login)
        self.assertEqual(response.status_code, 400)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    def test_blank_password_login(self):
        """Test that endpoint cannot login a user using blank password"""
        super().create_user(admin_user)
        response = super().login_user(blank_password_login)
        self.assertEqual(response.status_code, 400)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    def test_unexisting_login(self):
        """Test that endpoint cannot login an unexisting user"""
        response = super().login_user(unregistered_login)
        self.assertEqual(response.status_code, 403)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['message'] == 'That email is not registered')

    def test_blank_body_login(self):
        """Test that endpoint cannot login a user with empty request body"""
        super().create_user(admin_user)
        response = super().login_user(empty_body_login)
        self.assertEqual(response.status_code, 400)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)

    # def tearDown(self):
    #     return super().tearDown()


if __name__ == "__main__":
    unittest.main()
