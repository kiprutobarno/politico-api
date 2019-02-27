from app.api.v2.db import db
from utils.helpers import drop, insert, select, select_one, search, select_multiple_conditions, get_candidates


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
        cursor.execute(insert('candidates', candidates))
        self.db.commit()
        return candidates

    def update(self, candidate):
        query = """UPDATE users SET iscandidate=TRUE WHERE id={}""".format(
            candidate)
        cursor = self.db.cursor()
        cursor.execute(query)
        return self.db.commit()

    def get_politicians_specific_office(self, id):
        cursor = self.db.cursor()
        cursor.execute(get_candidates('offices.id', id))

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
        cursor.execute(select_multiple_conditions('candidates', office, party))
        data = cursor.fetchall()
        if len(data) > 0:
            return True

    def search_party(self, party):
        cursor = self.db.cursor()
        cursor.execute(select_one('parties', party))
        data = cursor.fetchall()
        if len(data) > 0:
            return True

    def search_office(self, office):
        cursor = self.db.cursor()
        cursor.execute(select_one('offices', office))
        data = cursor.fetchall()
        if len(data) > 0:
            return True

    def search(self, candidate):
        """This function returns True if a user is already a registered candidate."""
        cursor = self.db.cursor()
        cursor.execute(select_one('candidates', candidate))
        data = cursor.fetchall()
        if len(data) > 0:
            return True

    def get(self, id):
        cursor = self.db.cursor()
        cursor.execute(get_candidates('candidates.candidate', id))

        data = cursor.fetchone()
        return {
            "candidate": data[0]+" "+data[1],
            "office": data[2],
            "party": data[3],
        }
