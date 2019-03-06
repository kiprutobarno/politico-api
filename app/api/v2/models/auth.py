from passlib.hash import pbkdf2_sha256 as sha256
from app.api.v2.database.db import Connection


class User:
    """User Model"""

    def __init__(self):
        self.db = Connection()

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
        self.db.insert('users', user)

    def search(self, email):
        """ This function returns True if an email exists in the database."""
        if self.db.search_by_email('users', email):
            return True

    def login(self, email, password):
        """ This function verifies user password and returns "\
            "the user's isAdmin status """
        self.db.search_by_email('users', email)
        hashes = self.db.search_by_email('users', email)
        if User().verify_hash(password, hashes[8]):
            return hashes

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)
