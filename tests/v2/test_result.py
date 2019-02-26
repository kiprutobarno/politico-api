from .base_test import *


class ResultTestCase(BaseTestCase):
    """ This class represents the party test cases and inherits from BaseTestCase class """

    def test_result(self):
        """ Test that endpoint can enable a voter to vote"""
        super().create_user(user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        super().create_party(party, token)
        super().create_office(office, token)
        super().register_candidate(candidate, token)
        super().vote(ballot, token)
        response = super().get_results_specific_office(token)
        response_content = json.loads(response.data.decode('utf-8'))
        self.assertEqual(
            response_content['message'], "Election Results")

    def test_result_unavailable_office(self):
        """ Test that endpoint cannot return results for an unavailable office"""
        super().create_user(user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        super().create_party(party, token)
        super().create_office(office, token)
        super().register_candidate(candidate, token)
        super().vote(ballot, token)
        response = super().get_results_unavailable_office(token)
        response_content = json.loads(response.data.decode('utf-8'))
        self.assertEqual(
            response_content['message'], "Such an office was not available in this election cycle!")
