from app.api.v2.db import db
from utils.helpers import insert, get_all, drop, get_one, search, delete


class Party:
    """ The party model """

    def __init__(self):
        self.db = db()

    def create_party(self, name, hqAddress, logoUrl):
        """ Create a party method """
        party = {
            "name": name,
            "hqAddress": hqAddress,
            "logoUrl": logoUrl
        }

        cursor = self.db.cursor()
        cursor.execute(insert('parties', party))
        self.db.commit()
        return party

    def get_all_parties(self):
        """ Get all parties method """
        cursor = self.db.cursor()
        cursor.execute(get_all('parties'))
        data = cursor.fetchall()
        parties = []
        for i, items in enumerate(data):
            id, name, hqaddress, logourl = items
            party = dict(
                id=int(id),
                name=name,
                hqaddress=hqaddress,
                logourl=logourl
            )
            parties.append(party)
        return parties

    def get_specific_party(self, id):
        """ Get all parties method """
        cursor = self.db.cursor()
        cursor.execute(get_one('parties', id))
        data = cursor.fetchall()
        parties = []
        for i, items in enumerate(data):
            id, name, hqAddress, logourl, = items
            party = dict(
                id=int(id),
                name=name,
                hqAddress=hqAddress,
                logourl=logourl
            )
            parties.append(party)
        return parties

    def edit_party(self, id, name, data):
        """Update the details of a political party"""
        party = Party().get_specific_party(id)
        if Party().get_specific_party(id):
            if data.get('name') and data.get(
                    'hqAddress') and data.get('logoUrl'):
                cursor = self.db.cursor()
                cursor.execute(
                    "UPDATE parties SET name=%s, hqAddress=%s, logoUrl=%s WHERE id={}".format(
                        id, name), (data.get('name'), data.get('hqAddress'), data.get('logoUrl')))
                return self.db.commit()

    def delete_party(self, id):
        """This function deletes a product entry in the database"""
        cursor = self.db.cursor()
        cursor.execute(delete('parties', id))
        return self.db.commit()

    def search(self, name):
        """ This function returns True if an email exists in the database."""
        cursor = self.db.cursor()
        cursor.execute(search('parties', name))
        data = cursor.fetchall()
        if len(data) > 0:
            return True
