from passlib.hash import pbkdf2_sha256 as sha256
from app.api.v2.db import db
from utils.helpers import insert, select, drop, select_one, delete, search


class User:
    """User Model"""

    def __init__(self):
        self.db = db()

    def create_user(
            self,
            firstName,
            lastName,
            otherName,
            email,
            phoneNumber,
            passportUrl,
            password):
        """Save user details in the users table"""
        user = {
            "firstName": firstName,
            "lastName": lastName,
            "otherName": otherName,
            "email": email,
            "phoneNumber": phoneNumber,
            "passportUrl": passportUrl,
            "password": User.generate_hash(password)
        }

        cursor = self.db.cursor()
        cursor.execute(insert('users', user))
        self.db.commit()
        return user

    def search(self, email):
        """ This function returns True if an email exists in the database."""
        cursor = self.db.cursor()
        cursor.execute("""SELECT * FROM users WHERE email='%s'""" % (email))
        data = cursor.fetchall()
        if len(data) > 0:
            return True

    def login(self, email, password):
        """ This function verifies user password and returns "\
            "the user's is_admin status """
        cursor = self.db.cursor()
        cursor.execute("""SELECT * FROM users  WHERE email='%s'""" % (email))
        hashes = cursor.fetchone()
        if User().verify_hash(password, hashes[9]):
            return hashes

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)
