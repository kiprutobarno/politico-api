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
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)
        with self.app.app_context():
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

    # def edit_party(self, data):
    #     """Edit political party endpoint test method """
    #     return self.client.patch(
    #         '/api/v1/parties/1/Red',
    #         data=data,
    #         content_type='application/json'
    #     )

    # def delete_party(self):
    #     return self.client.delete(
    #         '/api/v1/parties/1',
    #         content_type='application/json',
    #     )

    # def invalid_delete_party(self):
    #     return self.client.delete(
    #         '/api/v1/parties/0',
    #         content_type='application/json',
    #     )

    # # Office test methods
    # def create_office(self, data):
    #     """Create office endpoint test method """
    #     return self.client.post(
    #         'api/v1/offices',
    #         data=data,
    #         content_type='application/json'
    #     )

    # def get_all_offices(self):
    #     """Get all offices endpoint test method """
    #     return self.client.get(
    #         '/api/v1/offices',
    #         content_type='application/json'
    #     )

    # def get_specific_office(self):
    #     """Get specific office endpoint test method """
    #     return self.client.get(
    #         '/api/v1/offices/1',
    #         content_type='application/json'
    #     )


    def teardown(self):
        with self.app.app_context():
            destroy_tables()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
