from app.api.v2.database.db import Connection


class Vote:
    """ The candidate model """

    def __init__(self):
        self.db = Connection()

    def vote(self, office, candidate, voter):
        """ Create a office method """
        vote = {
            "office": office,
            "candidate": candidate,
            "createdby": voter
        }
        self.db.insert('votes', vote)
        return vote

    def search_office(self, office):
        if self.db.fetch_single_item('offices', office):
            return True

    def search_candidate(self, candidate):
        """This function returns True if a user is already a registered candidate."""

        if self.db.fetch_single_item('nominations', candidate):
            return True

    def search(self, office, createdby):
        """ This function returns True if a user is already voted"""
        self.db.cursor.execute(
            """SELECT * FROM votes WHERE office={} AND createdby={}""".format(office, createdby))
        data = self.db.cursor.fetchall()
        if len(data) > 0:
            return True

    def get_candidate(self, id):
        self.db.cursor.execute(
            """SELECT users.firstname, users.lastname FROM users INNER JOIN nominations ON nominations.usr=users.id WHERE usr={}""".format(id))
        data = self.db.cursor.fetchone()
        return data

    def get(self, id):
        query = """ SELECT offices.name, users.firstname, users.lastname, nominations.usr, parties.name FROM votes
                    INNER JOIN offices ON votes.office=offices.id
                    INNER JOIN users ON votes.createdby=users.id
                    INNER JOIN nominations ON votes.candidate=nominations.usr
                    INNER JOIN parties ON nominations.party=parties.id""".format(id)
        self.db.cursor.execute(query)

        data = self.db.cursor.fetchone()
        print(data)
        return {
            "voter": data[1] +
            " " +
            data[2],
            "office": data[0],
            "candidate": Vote().get_candidate(data[3])[0] + " "+Vote().get_candidate(data[3])[1],
            "party": data[4],
            "message": "Success"
        }
