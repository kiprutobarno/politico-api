from passlib.hash import pbkdf2_sha256 as sha256
from app.api.v2.db import db

class User:
    """User Model"""

    def __init__(self):
        self.db=db()

    
    def create_user(self, firstName, lastName, otherName, email, phoneNumber, passportUrl, isAdmin, isCandidate, password):
        """Save user details in the users table"""
        user = {
            "firstName": firstName,
            "lastName": lastName,
            "otherName": otherName,
            "email": email,
            "phoneNumber": phoneNumber,
            "passportUrl": passportUrl,
            "isAdmin": isAdmin,
            "isCandidate": isCandidate,
            "password": User.generate_hash(password)
        }

        query = """INSERT INTO users(firstname, lastname, othername, email, phonenumber, passporturl, isadmin, iscandidate, password) VALUES(%(firstName)s, %(lastName)s, %(otherName)s, %(email)s, %(phoneNumber)s, %(passportUrl)s, %(isAdmin)s, %(isCandidate)s, %(password)s)"""
        cursor = self.db.cursor()
        cursor.execute(query, user)
        self.db.commit()
        return user

    
    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)
