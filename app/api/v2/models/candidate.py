from app.api.v2.db import db
from utils.helpers import drop, insert, get_all, get_one, search


class Candidate:
    """ The candidate model """

    def __init__(self):
        self.db = db()

    def register(self, office, party, candidate):
        """ Create a office method """
        candidates = {
            "office": office,
            "party": party,
            "candidate": candidate
        }
        cursor = self.db.cursor()
        cursor.execute("""INSERT INTO candidates(office, party, candidate) VALUES({}, {}, {}) """.format(
            office, party, candidate))
        self.db.commit()
        return candidates

    def update(self, candidate):
        query = """UPDATE users SET iscandidate=TRUE WHERE id={}""".format(
            candidate)
        cursor = self.db.cursor()
        cursor.execute(query)
        return self.db.commit()

    def get_politicians_specific_office(self, id):
        query = """ SELECT users.firstname, users.lastname, offices.name, parties.name
                    FROM candidates INNER JOIN users ON candidates.candidate=users.id
                    INNER JOIN offices ON candidates.office=offices.id
                    INNER JOIN parties ON candidates.party=parties.id WHERE offices.id={}""".format(id)
        cursor = self.db.cursor()
        cursor.execute(query)

        data = cursor.fetchall()
        rows = []
        for i, items in enumerate(data):
            firstname, lastname, office, party = items
            result = dict(
                office=office,
                candidate=firstname+" "+lastname,
                party=party
            )
            rows.append(result)

        return rows

    def party_has_candidate(self, office, party):
        cursor = self.db.cursor()
        cursor.execute(
            """SELECT * FROM candidates WHERE office={} AND party={}""".format(office, party))
        data = cursor.fetchall()
        if len(data) > 0:
            return True

    def search_party(self, party):
        cursor = self.db.cursor()
        cursor.execute("""SELECT * FROM parties WHERE id={}""".format(party))
        data = cursor.fetchall()
        if len(data) > 0:
            return True

    def search_office(self, office):
        cursor = self.db.cursor()
        cursor.execute("""SELECT * FROM offices WHERE id={}""".format(office))
        data = cursor.fetchall()
        if len(data) > 0:
            return True

    def search(self, candidate):
        """This function returns True if a user is already a registered candidate."""
        cursor = self.db.cursor()
        cursor.execute(
            """SELECT * FROM candidates WHERE candidate={}""".format(candidate))
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
            "candidate": data[0]+" "+data[1],
            "office": data[2],
            "party": data[3],
        }
