from app.api.v2.db import create_tables, destroy_tables
from utils.dummy import *
from unittest import TestCase
from app import create_app
from utils.dummy import *
import os
import unittest
import sys
sys.path.append('../../')


class BaseTestCase(TestCase):
    """ Base Tests """

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.app.config['TESTING'] = True
        self.client = self.app.test_client(use_cookies=True)
        create_tables()

    def create_user(self, data):
        """Create user endpoint test methods"""
        return self.client.post(
            'api/v2/auth/signup',
            data=data,
            content_type='application/json'
        )

    def login_user(self, data):
        """User login endpoint test method"""
        return self.client.post(
            'api/v2/auth/login',
            data=data,
            content_type='application/json'
        )

    # Party test methods
    def create_party(self, data, token):
        """Create party endpoint test method """
        return self.client.post(
            'api/v2/parties',
            data=data,
            content_type='application/json',
            headers=dict(Authorization="Bearer " + token)
        )

    def get_all_parties(self, token):
        """Get all parties endpoint test method """
        return self.client.get(
            '/api/v2/parties',
            content_type='application/json',
            headers=dict(Authorization="Bearer " + token)
        )

    def get_specific_party(self, token):
        """Get specific party endpoint test method """
        return self.client.get(
            '/api/v2/parties/1',
            content_type='application/json',
            headers=dict(Authorization="Bearer " + token)
        )

    def get_specific_party_invalid(self, token):
        """Get specific party endpoint test method """
        return self.client.get(
            '/api/v2/parties/0',
            content_type='application/json',
            headers=dict(Authorization="Bearer " + token)
        )

    def edit_party(self, data, token):
        """Edit political party endpoint test method """
        return self.client.patch(
            '/api/v2/parties/1/Red',
            data=data,
            content_type='application/json',
            headers=dict(Authorization="Bearer " + token)
        )

    def edit_party_invalid(self, data, token):
        """Edit political party endpoint test method """
        return self.client.patch(
            '/api/v2/parties/0/Red',
            data=data,
            content_type='application/json',
            headers=dict(Authorization="Bearer " + token)
        )

    def delete_party(self, token):
        return self.client.delete(
            '/api/v2/parties/1',
            content_type='application/json',
            headers=dict(Authorization="Bearer " + token)
        )

    def invalid_delete_party(self, token):
        return self.client.delete(
            '/api/v2/parties/0',
            content_type='application/json',
            headers=dict(Authorization="Bearer " + token)
        )

    # Office test methods
    def create_office(self, data, token):
        """Create office endpoint test method """
        return self.client.post(
            'api/v2/offices',
            data=data,
            content_type='application/json',
            headers=dict(Authorization="Bearer " + token)
        )

    def get_all_offices(self, token):
        """Get all offices endpoint test method """
        return self.client.get(
            '/api/v2/offices',
            content_type='application/json',
            headers=dict(Authorization="Bearer " + token)
        )

    def get_specific_office(self, token):
        """Get specific office endpoint test method """
        return self.client.get(
            '/api/v2/offices/1',
            content_type='application/json',
            headers=dict(Authorization="Bearer " + token)
        )

    def get_specific_office_invalid(self, token):
        """Get specific office endpoint test method """
        return self.client.get(
            '/api/v2/offices/0',
            content_type='application/json',
            headers=dict(Authorization="Bearer " + token)
        )

    # candidate test methods
    def register_candidate(self, data, token):
        """Create candidate endpoint test method """
        return self.client.post(
            'api/v2/office/1/register',
            data=data,
            content_type='application/json',
            headers=dict(Authorization="Bearer " + token)
        )

    def get_specifc_office_candidates(self, token):
        """Create candidate endpoint test method """
        return self.client.get(
            'api/v2/office/1/candidates',
            content_type='application/json',
            headers=dict(Authorization="Bearer " + token)
        )

    # result test methods
    def get_results_specific_office(self, token):
        """Create candidate endpoint test method """
        return self.client.get(
            'api/v2/office/1/result',
            content_type='application/json',
            headers=dict(Authorization="Bearer " + token)
        )

    def get_results_unavailable_office(self, token):
        """Create candidate endpoint test method """
        return self.client.get(
            'api/v2/office/2/result',
            content_type='application/json',
            headers=dict(Authorization="Bearer " + token)
        )

    # vote test methods
    def vote(self, data, token):
        return self.client.post(
            'api/v2/votes/',
            data=data,
            content_type='application/json',
            headers=dict(Authorization="Bearer " + token)
        )

    def tearDown(self):
        with self.app.app_context():
            destroy_tables()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
