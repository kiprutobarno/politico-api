from app.api.v2.database.db import Connection


class Office:
    """ The office model """

    def __init__(self):
        self.db = Connection()

    def create_office(self, name, officeType):
        """ Create a office method """
        office = {
            "name": name,
            "type": officeType
        }
        self.db.insert('offices', office)
        return office

    def get_all_offices(self):
        """ Get all offices method """
        data = self.db.fetch_all_items('offices')
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
        """ Get specific office method """
        data = self.db.fetch_single_item('offices', id)
        for i, items in enumerate(data):
            id, name, officeType = items
            office = dict(
                id=int(id),
                name=name,
                officeType=officeType
            )
            return office

    def search(self, name):
        """ This function returns True if an office name already exists in the database."""
        if self.db.search_by_name('offices', name):
            return True
