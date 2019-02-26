from .base_test import *
from app.api.v2.db import connection, db
from flask import current_app


class DBTestCase(BaseTestCase):
    """ This class represents database test cases and inherits from BaseTestCase class """

    def test_db_connection(self):
        """ Test that database connection is successful"""
        connection()

    def test_db_object_created(self):
        db()
