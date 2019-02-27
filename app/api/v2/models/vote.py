from app.api.v2.database.db import insert, fetch_all_items, fetch_single_item, delete, search_by_name, connection


class Vote:
    """ The candidate model """

    def vote(self, office, candidate, voter):
        """ Create a office method """
        vote = {
            "office": office,
            "candidate": candidate,
            "createdby": voter
        }
        insert('votes', vote)
        return vote

    def search_office(self, office):
        if fetch_single_item('offices', office):
            return True

    def search_candidate(self, candidate):
        """This function returns True if a user is already a registered candidate."""

        if fetch_single_item('candidates', candidate):
            return True

    def search(self, office, createdby):
        """ This function returns True if a user is already voted"""
        cursor = connection().cursor()
        cursor.execute(
            """SELECT * FROM votes WHERE office={} AND createdby={}""".format(office, createdby))
        data = cursor.fetchall()
        if len(data) > 0:
            return True

    def get_candidate(self, id):
        cursor = connection().cursor()
        cursor.execute(
            """SELECT users.firstname, users.lastname FROM users INNER JOIN candidates ON candidates.candidate=users.id WHERE candidate={}""".format(id))
        data = cursor.fetchone()
        return data

    def get(self, id):
        query = """ SELECT offices.name, users.firstname, users.lastname, candidates.candidate FROM votes
                    INNER JOIN offices ON votes.office=offices.id
                    INNER JOIN users ON votes.createdby=users.id
                    INNER JOIN candidates ON votes.candidate=candidates.candidate
                    """.format(id)
        cursor = connection().cursor()
        cursor.execute(query)

        data = cursor.fetchone()
        return {
            "voter": data[1] +
            " " +
            data[2],
            "office": data[0],
            "candidate": Vote().get_candidate(data[3])[0] + " "+Vote().get_candidate(data[3])[1],
            "message": "Success"
        }
