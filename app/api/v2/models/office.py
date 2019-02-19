from app.api.v2.db import db
class Office:
    """ The office model """
    def __init__(self):
        self.db=db()

    def create_office(self, name, officeType):
        """ Create a office method """
        office = {
            "name": name,
            "officeType": officeType
        }
        
        query = """INSERT INTO offices(name, type) VALUES(%(name)s, %(officeType)s)"""
        cursor = self.db.cursor()
        cursor.execute(query, office)
        self.db.commit()
        return office   
