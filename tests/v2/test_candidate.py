from .base_test import *


class CandidateTestCase(BaseTestCase):
    """ This class represents candidate test cases and inherits from BaseTestCase class """

    def test_register_candidate(self):
        """ Test that endpoint can create office"""
        super().create_user(user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        super().create_party(party, token)
        super().create_office(office, token)
        response = super().register_candidate(candidate, token)
        response_content = json.loads(response.data.decode('utf-8'))
        self.assertEqual(
            response_content['message'], "Candidate registration successfull!")

    def test_register_existing_candidate(self):
        """ Test that endpoint cannot create an existing office"""
        super().create_user(user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        super().create_party(party, token)
        super().create_office(office, token)
        super().register_candidate(candidate, token)
        response = super().register_candidate(candidate, token)
        response_content = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_content['status'], 400)

    def test_party_cannot_register_two_candidates(self):
        """ Test that endpoint cannot create an existing office"""
        super().create_user(user)
        super().create_user(user1)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        super().create_party(party, token)
        super().create_office(office, token)
        super().register_candidate(candidate, token)
        response = super().register_candidate(candidate1, token)
        response_content = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_content['status'], 400)

    def test_get_specific_office_candidates(self):
        """ Test that endpoint can create office"""
        super().create_user(user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        super().create_party(party, token)
        super().create_office(office, token)
        super().register_candidate(candidate, token)
        response = super().get_specifc_office_candidates(token)
        response_content = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_content['message'], "Success")
