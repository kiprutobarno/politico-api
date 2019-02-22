from app.api.v2.db import db
from utils.helpers import insert, get_all, drop, get_one, delete, search


class Vote:
    """ The candidate model """

    def __init__(self):
        self.db = db()

    def vote(self, office, candidate, voter):
        """ Create a office method """
        vote = {
            "office": office,
            "candidate": candidate,
            "createdby": voter
        }
        cursor = self.db.cursor()
        cursor.execute(insert('votes', vote))
        self.db.commit()
        return vote

    def search_office(self, office):
        cursor = self.db.cursor()
        cursor.execute("""SELECT * FROM offices WHERE id={}""".format(office))
        # cursor.execute(search('candidates', id))
        data = cursor.fetchall()
        if len(data) > 0:
            return True

    def search_candidate(self, candidate):
        """This function returns True if a user is already a registered candidate."""
        cursor = self.db.cursor()
        cursor.execute("""SELECT * FROM candidates WHERE candidate={}""".format(candidate))
        # cursor.execute(search('candidates', id))
        data = cursor.fetchall()
        if len(data) > 0:
            return True

    def search(self, createdby):
        """ This function returns True if a user is already voted"""
        cursor = self.db.cursor()
        cursor.execute(
            """SELECT * FROM votes WHERE createdby={}""".format(createdby))
        # cursor.execute(search('votes', createdby))
        data = cursor.fetchall()  # tuple
        if len(data) > 0:
            return True

    def get(self, id):
        query = """ SELECT offices.name, users.firstname, users.lastname, candidates.candidate FROM votes
                    INNER JOIN offices ON votes.office=offices.id
                    INNER JOIN candidates ON votes.candidate=candidates.candidate
                    INNER JOIN users ON votes.createdby=users.id""".format(id)
        cursor = self.db.cursor()
        cursor.execute(query)

        data = cursor.fetchone()
        return {
            "voter": data[1] +
            " " +
            data[2],
            "office": data[0],
            "candidate": data[3]}
