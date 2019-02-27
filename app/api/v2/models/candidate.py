from app.api.v2.database.db import insert, fetch_all_items, fetch_single_item, delete, search_by_name, connection, fetch_all_candidates, fetch_item_multiple_conditions, fetch_candidate


class Candidate:
    """ The candidate model """

    def register(self, office, party, candidate):
        """ Create a office method """
        candidates = {
            "office": office,
            "party": party,
            "candidate": candidate
        }

        insert('candidates', candidates)
        return candidates

    def update(self, candidate):
        query = """UPDATE users SET iscandidate=TRUE WHERE id={}""".format(
            candidate)
        cursor = connection().cursor()
        cursor.execute(query)
        return connection().commit()

    def get_politicians_specific_office(self, id):
        data = fetch_all_candidates('offices.id', id)
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
        if fetch_item_multiple_conditions('candidates', office, party):
            return True

    def search_party(self, party):
        if fetch_single_item('parties', party):
            return True

    def search_office(self, office):
        if fetch_single_item('offices', office):
            return True

    def search(self, candidate):
        """This function returns True if a user is already a registered candidate."""
        if fetch_single_item('candidates', candidate):
            return True

    def get(self, id):
        data = fetch_candidate('candidates.candidate', id)
        return {
            "candidate": data[0]+" "+data[1],
            "office": data[2],
            "party": data[3],
        }
