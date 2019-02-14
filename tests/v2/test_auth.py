from .base_test import *

class UserTestCase(BaseTestCase):
    """ This class represents the user test cases and inherits from BaseTestCase class """
    
    def setUp(self):
        super().setUp()

    def test_create_user(self):
        """ Test that endpoint can create user"""
        response = super().create_user(admin_user)
        self.assertEqual(response.status_code, 201)
        response_content =  json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 201)

    def test_user_login(self):
        """Test that endpoint can login a registered user"""
        super().create_user(admin_user)
        response = super().login_user(admin_user_login)
        self.assertEqual(response.status_code, 200)
        response_content =  json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 200)

    def tearDown(self):
        return super().tearDown()
        
if __name__ == "__main__":
    unittest.main()