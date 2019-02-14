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

    def teardown(self):
        with self.app.app_context():
            destroy_tables()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
