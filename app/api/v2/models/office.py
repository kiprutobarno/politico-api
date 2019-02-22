from app.api.v2.db import db
from utils.helpers import insert, get_all, drop, get_one, search

class Office:
    """ The office model """

    def __init__(self):
        self.db = db()

    def create_office(self, name, officeType):
        """ Create a office method """
        office = {
            "name": name,
            "type": officeType
        }

        cursor = self.db.cursor()
        cursor.execute(insert('offices', office))
        self.db.commit()
        return office

    def get_all_offices(self):
        """ Get all parties method """
        cursor = self.db.cursor()
        cursor.execute(get_all('offices'))
        data = cursor.fetchall()
        offices = []
        for i, items in enumerate(data):
            id, name, officeType = items
            office = dict(
                id=int(id),
                name=name,
                officeType=officeType
            )
            offices.append(office)
        return offices

    def get_specific_office(self, id):
        """ Get all parties method """
        cursor = self.db.cursor()
        cursor.execute(get_one('offices', id))
        data = cursor.fetchall()
        offices = []
        for i, items in enumerate(data):
            id, name, officeType = items
            office = dict(
                id=int(id),
                name=name,
                officeType=officeType
            )
            offices.append(office)
        return offices

    def search(self, name):
        """ This function returns True if an email exists in the database."""
        cursor = self.db.cursor()
        cursor.execute(search('offices', name))
        data = cursor.fetchall()
        if len(data) > 0:
            return True
