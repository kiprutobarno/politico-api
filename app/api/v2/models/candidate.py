from app.api.v2.database.db import Connection


class Candidate:
    """ The candidate model """

    def __init__(self):
        self.db = Connection()

    def approve(self, candidate):
        query = """UPDATE nominations SET approved=TRUE, dateapproved=NOW() WHERE usr={}""".format(
            candidate)

        self.db.cursor.execute(query)
        return self.db.connection.commit()

    def checkApproved(self, candidate):
        if self.db.fetch_approved_candidate(candidate):
            return True

    def unApprove(self, candidate):
        if self.checkApproved(candidate):
            query = """UPDATE nominations SET approved=FALSE, dateapproved=NOW() WHERE usr={}""".format(
                candidate)

            self.db.cursor.execute(query)
            return self.db.connection.commit()

    def getParty(self, candidate):
        data = self.db.fetch_party(candidate)
        party = data[0]
        return party

    def getOffice(self, candidate):
        data = self.db.fetch_office(candidate)
        party = data[0]
        return party

    def get_all_politicians(self):
        """Fetch all politicians"""
        data = self.db.fetch_all_politicians()
        rows = []
        for i, items in enumerate(data):
            id, user, firstname, lastname, othername, office, party, dateapplied, approved, dateapproved = items
            result = dict(
                id=id,
                usr=user,
                office=office,
                firstname=firstname,
                othername=othername,
                lastname=lastname,
                party=party,
                dateapplied=dateapplied,
                approved=approved,
                dateapproved=dateapproved
            )
            rows.append(result)

        return rows

    def get_all_candidates(self):
        """Get all candidates"""
        data = self.db.fetch_all_candidates()
        rows = []
        for i, items in enumerate(data):
            id, user, firstname, lastname, othername, office, party, dateapplied, approved, dateapproved = items
            result = dict(
                id=id,
                usr=user,
                office=office,
                firstname=firstname,
                othername=othername,
                lastname=lastname,
                party=party,
                dateapplied=dateapplied,
                approved=approved,
                dateapproved=dateapproved
            )
            rows.append(result)

        return rows

    def get_candidates_per_office(self, id):
        """Get candidates per office"""
        data = self.db.fetch_candidates_per_office(id)
        rows = []
        for i, items in enumerate(data):
            id, user, firstname, lastname, othername, office, party, dateapplied, approved, dateapproved = items
            result = dict(
                id=id,
                usr=user,
                office=office,
                firstname=firstname,
                othername=othername,
                lastname=lastname,
                party=party,
                dateapplied=dateapplied,
                approved=approved,
                dateapproved=dateapproved
            )
            rows.append(result)

        return rows

    def party_has_candidate(self, candidate):
        if self.db.fetch_party_approved_candidate(self.getParty(candidate), self.getOffice(candidate)):
            return True

    def search(self, candidate):
        """This function returns True if a user is already a registered candidate."""
        if self.db.fetch_single_item('candidates', candidate):
            return True

    def get(self, id):
        data = self.db.fetch_candidate('nominations.usr', id)
        return {
            "candidate": data[0]+" "+data[1],
            "office": data[2],
            "party": data[3],
        }
