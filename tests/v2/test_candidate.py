# from .base_test import *

# class CandidateTestCase(BaseTestCase):
#     """ This class represents the party test cases and inherits from BaseTestCase class """

#     def setUp(self):
#         super().setUp()

#     def test_register_candidate(self):
#         """ Test that endpoint can create office"""
#         super().create_user(user)
#         login=super().login_user(admin_user_login)
#         login_content = json.loads(login.data.decode('utf-8'))
#         token=[d['token'] for d in login_content['data']][0]
#         response=super().register_candidate(candidate, token)
#         response_content =  json.loads(response.data.decode('utf-8'))
#         self.assertTrue(response_content['status'] == 201)
