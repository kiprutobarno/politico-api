from app.api.v2.db import db


class Vote:
    """ The candidate model """

    def __init__(self):
        self.db = db()

    def vote(self, office, candidate, voter):
        """ Create a office method """
        vote = {
            "office": office,
            "candidate": candidate,
            "voter": voter
        }
        query = """INSERT INTO votes(office, candidate, createdby) VALUES(%(office)s, %(candidate)s, %(voter)s)"""
        cursor = self.db.cursor()
        cursor.execute(query, vote)
        self.db.commit()
        return vote

    def get(self, id):
        query = """ SELECT offices.name, users.firstname, users.lastname, candidates.candidate FROM votes 
                    INNER JOIN offices ON votes.office=offices.id
                    INNER JOIN candidates ON votes.candidate=candidates.candidate
                    INNER JOIN users ON votes.createdby=users.id""".format(id)
        cursor = self.db.cursor()
        cursor.execute(query)

        data = cursor.fetchone()
        print(data)
        return { "voter": data[1]+" "+data[2], "office": data[0], "candidate": data[3]}
        
