from app.api.v2.db import db


class Result:
    """ The candidate model """

    def __init__(self):
        self.db = db()

    def get(self, id):
        query = """SELECT offices.name, users.firstname, users.lastname, COUNT(*) as votes FROM votes
                   INNER JOIN offices ON offices.id=votes.office
                   INNER JOIN users ON users.id=votes.candidate WHERE office={}
                   GROUP BY offices.name, users.firstname, users.lastname;""".format(id)
        cursor = self.db.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        rows = []
        for i, items in enumerate(data):
            office, firstname, lastname, results = items
            result = dict(
                office=office,
                candidate=firstname+" "+lastname,
                results=results
            )
            rows.append(result)

        return rows

    def search(self, office):
        """ This function returns True if an office is available for election"""
        cursor = self.db.cursor()
        cursor.execute(
            """SELECT * FROM offices WHERE id={}""".format(office))
        # cursor.execute(search('votes', createdby))print(Vote().get_candidate(candidate)[0][0])
        data = cursor.fetchall()
        if len(data) > 0:
            return True
