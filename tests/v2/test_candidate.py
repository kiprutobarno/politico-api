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

    def test_register_no_office_candidate(self):
        """ Test that endpoint can create office"""
        super().create_user(user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        super().create_party(party, token)
        response = super().register_candidate(candidate, token)
        response_content = json.loads(response.data.decode('utf-8'))
        self.assertEqual(
            response_content['message'], "Such an office is not available, please confirm again!")

    def test_register_no_party_candidate(self):
        """ Test that endpoint can create office"""
        super().create_user(user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        super().create_office(office, token)
        response = super().register_candidate(candidate, token)
        response_content = json.loads(response.data.decode('utf-8'))
        self.assertEqual(
            response_content['message'], "Such a party is not registered, please confirm again!")

    def test_register_blank_candidate(self):
        """ Test that endpoint can create office"""
        super().create_user(user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        super().create_party(party, token)
        super().create_office(office, token)
        response = super().register_candidate(candidate_blank, token)
        response_content = json.loads(response.data.decode('utf-8'))
        self.assertEqual(
            response_content['message'], "office cannot be blank")

    def test_register_nonint_candidate(self):
        """ Test that endpoint can create office"""
        super().create_user(user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        super().create_party(party, token)
        super().create_office(office, token)
        response = super().register_candidate(string_candidate, token)
        response_content = json.loads(response.data.decode('utf-8'))
        self.assertEqual(
            response_content['message'], "party must be an integer")

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
