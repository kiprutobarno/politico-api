import os
import unittest
import sys
sys.path.append('../../')
from app import create_app
from unittest import TestCase
from utils.helper_data import *
from .helper_methods import *
   

class BaseTestCase(TestCase):
    """ Base Tests """

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    
    def teardown(self):
        self.app_context.pop()