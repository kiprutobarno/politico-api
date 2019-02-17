from app.api.v2.db import db


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
        query = """INSERT INTO candidates(office, party, candidate) VALUES(%(office)s, %(party)s, %(candidate)s)"""
        cursor = self.db.cursor()
        cursor.execute(query, candidate)
        self.db.commit()
        return candidate

    def update(self, candidate):
        query = """UPDATE users SET iscandidate=TRUE WHERE id={}""".format(candidate)
        cursor = self.db.cursor()
        cursor.execute(query)
        return self.db.commit()

    def get(self, id):
        query = """ SELECT users.firstname, users.lastname, offices.name, parties.name
                    FROM candidates INNER JOIN users ON candidates.candidate=users.id 
                    INNER JOIN offices ON candidates.office=offices.id 
                    INNER JOIN parties ON candidates.party=parties.id WHERE candidates.candidate={}""".format(id)
        cursor = self.db.cursor()
        cursor.execute(query)

        data = cursor.fetchone()
        return { "candidate": data[0]+" "+data[1], "office": data[2], "party": data[3]}
        
