from .base_test import *


class AuthTestCase(BaseTestCase):
    """ This class represents the user test cases and inherits from BaseTestCase class """

    def test_create_user(self):
        """ Test that endpoint can create user"""
        response = super().create_user(admin_user)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['message']
                        == "Registration successful!")

    def test_create_missingkey_user(self):
        """ Test that endpoint can create user"""
        response = super().create_user(missing_key_user)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['message'] == "firstName key missing")

    def test_create_weakpassword_user(self):
        """ Test that endpoint can create user"""
        response = super().create_user(weak_password_user)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['message'] == "Weak password!")

    def test_create_blankname_user(self):
        """ Test that endpoint can create user"""
        response = super().create_user(blank_user)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['message']
                        == "firstName cannot be blank")

    def test_create_user_non_string(self):
        """ Test that endpoint can create user"""
        response = super().create_user(int_user)
        response_content = json.loads(response.data.decode())
        self.assertEqual(
            response_content['message'], "firstName must be a string")

    def test_create_user_invalid_image(self):
        """ Test that endpoint can create user"""
        response = super().create_user(invalid_image_user)
        response_content = json.loads(response.data.decode())
        self.assertEqual(
            response_content['message'], "invalid image url")

    def test_create_user_invalid_email(self):
        """ Test that endpoint can create user"""
        response = super().create_user(invalid_email_user)
        response_content = json.loads(response.data.decode())
        self.assertEqual(
            response_content['message'], "invalid email address")

    def test_user_login(self):
        """Test that endpoint can login a registered user"""
        super().create_user(admin_user)
        response = super().login_user(admin_user_login)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 201)

    def test_wrong_password_login(self):
        """Test that endpoint cannot login a user using wrong password"""
        super().create_user(admin_user)
        response = super().login_user(wrong_password_login)
        self.assertEqual(response.status_code, 401)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['message']
                        == 'wrong login credentials')

    def test_blank_email_login(self):
        """Test that endpoint cannot login a user using blank email"""
        super().create_user(admin_user)
        response = super().login_user(blank_email_login)
        self.assertEqual(response.status_code, 400)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['message'] == "email cannot be blank")

    def test_invalid_email_login(self):
        """Test that endpoint cannot login a user using blank email"""
        super().create_user(admin_user)
        response = super().login_user(invalid_email_login)
        self.assertEqual(response.status_code, 400)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['message'] == "invalid email address")

    def test_blank_password_login(self):
        """Test that endpoint cannot login a user using blank password"""
        super().create_user(admin_user)
        response = super().login_user(blank_password_login)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['message']
                        == "password cannot be blank")

    def test_unexisting_login(self):
        """Test that endpoint cannot login unexisting user"""
        response = super().login_user(unregistered_login)
        response_content = json.loads(response.data.decode())
        self.assertTrue(
            response_content['message'] == 'That email is not registered')

    def test_blank_body_login(self):
        """Test that endpoint cannot login a user with empty request body"""
        super().create_user(admin_user)
        response = super().login_user(empty_body_login)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 400)


if __name__ == "__main__":
    unittest.main()
