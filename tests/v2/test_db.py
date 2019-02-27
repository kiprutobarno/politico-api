from .base_test import *
from app.api.v2.database.db import Connection
from flask import current_app


class DBTestCase(BaseTestCase):
    """ This class represents database test cases and inherits from BaseTestCase class """

    def test_db_connection(self):
        """ Test that database connection is successful"""
        Connection()

    def test_db_object_created(self):
        Connection().connection
