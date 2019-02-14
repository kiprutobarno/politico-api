from app.api.v2.db import db


class Blacklist:
    """Token blacklist model"""

    def __init__(self):
        self.db = db()

    def revoke_token(self, token, token_type, admin, issued_at, expires_at):
        """This function revokes and stores the revoked token in the blacklist table"""
        token = {
            "token": token,
            "token_type": token_type,
            "admin": admin,
            "issued_at": issued_at,
            "expires_at": expires_at
        }

        query = """INSERT INTO blacklists(token, token_type, admin, issued_at, expires_at) VALUES(%(token)s, %(token_type)s, %(admin)s, %(issued_at)s, %(expires_at)s) """

        cursor = self.db.cursor()
        cursor.execute(query, token)
        self.db.commit()
        return True

    def search(self, token):
        """This function returns True if a token exists in the blacklist table """
        conn = self.db()
        cursor = conn.cursor()
        cursor.execute(
            """ SELECT token from blacklists WHERE token='%s'""" % (token), token)
        if len(cursor.fetchall()) > 0:
            return True
