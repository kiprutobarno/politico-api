from app.api.v2.database.db import Connection


class Candidate:
    """ The candidate model """

    def __init__(self):
        self.db = Connection()

    def register(self, office, party, candidate):
        """ Create a office method """
        candidates = {
            "office": office,
            "party": party,
            "candidate": candidate
        }

        self.db.insert('candidates', candidates)
        return candidates

    def update(self, candidate):
        query = """UPDATE users SET iscandidate=TRUE WHERE id={}""".format(
            candidate)

        self.db.cursor.execute(query)
        return self.db.connection.commit()

    def get_politicians_specific_office(self, id):
        data = self.db.fetch_all_candidates('offices.id', id)
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
        if self.db.fetch_item_multiple_conditions('candidates', office, party):
            return True

    def search_party(self, party):
        if self.db.fetch_single_item('parties', party):
            return True

    def search_office(self, office):
        if self.db.fetch_single_item('offices', office):
            return True

    def search(self, candidate):
        """This function returns True if a user is already a registered candidate."""
        if self.db.fetch_single_item('candidates', candidate):
            return True

    def get(self, id):
        data = self.db.fetch_candidate('candidates.candidate', id)
        return {
            "candidate": data[0]+" "+data[1],
            "office": data[2],
            "party": data[3],
        }
