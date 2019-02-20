from app.api.v2.db import db
from utils.helpers import drop, insert, get_all, get_one, search


class Candidate:
    """ The candidate model """

    def __init__(self):
        self.db = db()

    def register(self, office, party, candidate):
        """ Create a office method """
        candidate = {
            "office": office,
            "party": party,
            "candidate": candidate
        }
        cursor = self.db.cursor()
        cursor.execute(insert('candidates', candidate))
        self.db.commit()
        return candidate

    def update(self, candidate):
        query = """UPDATE users SET iscandidate=TRUE WHERE id={}""".format(
            candidate)
        cursor = self.db.cursor()
        cursor.execute(query)
        return self.db.commit()

    def search_party(self, party):
        cursor = self.db.cursor()
        cursor.execute("""SELECT * FROM parties WHERE id={}""".format(party))
        # cursor.execute(search('candidates', id))
        data = cursor.fetchall()
        if len(data) > 0:
            return True

    def search_office(self, office):
        cursor = self.db.cursor()
        cursor.execute("""SELECT * FROM offices WHERE id={}""".format(office))
        # cursor.execute(search('candidates', id))
        data = cursor.fetchall()
        if len(data) > 0:
            return True

    def search(self, candidate):
        """This function returns True if a user is already a registered candidate."""
        cursor = self.db.cursor()
        cursor.execute(
            """SELECT * FROM candidates WHERE candidate={}""".format(candidate))
        # cursor.execute(search('candidates', id))
        data = cursor.fetchall()
        if len(data) > 0:
            return True

    def get(self, id):
        query = """ SELECT users.firstname, users.lastname, offices.name, parties.name
                    FROM candidates INNER JOIN users ON candidates.candidate=users.id
                    INNER JOIN offices ON candidates.office=offices.id
                    INNER JOIN parties ON candidates.party=parties.id WHERE candidates.candidate={}""".format(id)
        cursor = self.db.cursor()
        cursor.execute(query)

        data = cursor.fetchone()
        return {
            "candidate": data[0],
            "office": data[2],
            "party": data[3]}
        return data
