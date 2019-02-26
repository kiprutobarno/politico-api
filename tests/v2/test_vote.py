from .base_test import *
from app.api.v2.models.vote import Vote


class VoteTestCase(BaseTestCase):
    """ This class represents vote test cases and inherits from BaseTestCase class """

    def test_vote(self):
        """ Test that endpoint can enable a voter to vote"""
        super().create_user(user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        super().create_party(party, token)
        super().create_office(office, token)
        super().register_candidate(candidate, token)
        response = super().vote(ballot, token)
        response_content = json.loads(response.data.decode('utf-8'))
        self.assertEqual(
            response_content['message'], "Thanks for voting, your vote will count!")

    def test_vote_nonexistent_office(self):
        """ Test that endpoint cannot allow a voter to vote uncreated office"""
        super().create_user(user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        super().create_party(party, token)
        super().create_office(office, token)
        super().register_candidate(candidate, token)
        response = super().vote(no_office_ballot, token)
        response_content = json.loads(response.data.decode('utf-8'))
        self.assertEqual(
            response_content['message'], "Sorry, such elective office is not available!")

    def test_vote_nonexistent_candidate(self):
        """ Test that endpoint cannot allow a voter to vote for unregistered candidate"""
        super().create_user(user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        super().create_party(party, token)
        super().create_office(office, token)
        super().register_candidate(candidate, token)
        response = super().vote(no_candidate_ballot, token)
        response_content = json.loads(response.data.decode('utf-8'))
        self.assertEqual(
            response_content['message'], "Sorry, such a candidate is not registered!")

    def test_vote_twice(self):
        """ Test that endpoint cannot allow user to vote twice"""
        super().create_user(user)
        login = super().login_user(admin_user_login)
        login_content = json.loads(login.data.decode('utf-8'))
        token = [d['token'] for d in login_content['data']][0]
        super().create_party(party, token)
        super().create_office(office, token)
        super().register_candidate(candidate, token)
        super().vote(ballot, token)
        response = super().vote(ballot, token)
        response_content = json.loads(response.data.decode('utf-8'))
        self.assertEqual(
            response_content['message'], "Sorry, you have already voted!")
