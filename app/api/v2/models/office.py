from app.api.v2.db import db
class Office:
    """ The office model """
    def __init__(self):
        self.db=db()

    def create_office(self, officeType, name):
        """ Create a office method """
        office = {
            "officeType": officeType,
            "name": name
        }
        
        query = """INSERT INTO offices(name, type) VALUES(%(name)s, %(officeType)s)"""
        cursor = self.db.cursor()
        cursor.execute(query, office)
        self.db.commit()
        return office   
