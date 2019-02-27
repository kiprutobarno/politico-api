from app.api.v2.database.db import insert, fetch_all_items, fetch_single_item, delete, search_by_name


class Office:
    """ The office model """

    def create_office(self, name, officeType):
        """ Create a office method """
        office = {
            "name": name,
            "type": officeType
        }
        insert('offices', office)
        return office

    def get_all_offices(self):
        """ Get all offices method """
        data = fetch_all_items('offices')
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
        data = fetch_single_item('offices', id)
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
        """ This function returns True if an office name already exists in the database."""
        if search_by_name('offices', name):
            return True
