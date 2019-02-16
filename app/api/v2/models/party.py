from app.api.v2.db import db
class Party:
    """ The party model """
    def __init__(self):
        self.db=db()

    def create_party(self, name, hqAddress, logoUrl):
        """ Create a party method """
        party = {
            "name": name,
            "hqAddress": hqAddress,
            "logoUrl": logoUrl
        }
        
        query = """INSERT INTO parties(name, hqaddress, logourl) VALUES(%(name)s, %(hqAddress)s, %(logoUrl)s)"""
        cursor = self.db.cursor()
        cursor.execute(query, party)
        self.db.commit()
        return party  

    def get_all_parties(self):
        """ Get all parties method """
        cursor = self.db.cursor()
        cursor.execute("""SELECT id, name, hqaddress, logourl FROM parties""")
        data=cursor.fetchall()
        parties=[]
        for i, items in enumerate(data):
            id, name, hqaddress, logourl=items
            party=dict(
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
        cursor.execute("""SELECT id, name, hqaddress, logourl FROM parties WHERE id={}""".format(id))
        data=cursor.fetchall()
        parties=[]
        for i, items in enumerate(data):
            id, name, hqaddress, logourl=items
            party=dict(
                id=int(id),
                name=name,
                hqaddress=hqaddress,
                logourl=logourl
            )
            parties.append(party)
        return parties

    def delete_party(self, id):
        """This function deletes a product entry in the database"""
        cursor = self.db.cursor()
        cursor.execute("""DELETE FROM parties WHERE id={}""".format(id))
        return self.db.commit() 

    def search(self, name):
        """ This function returns True if an email exists in the database."""
        cursor=self.db.cursor()
        cursor.execute("""SELECT * FROM parties WHERE name='%s'"""%(name))
        data=cursor.fetchall() #tuple
        if len(data)>0:
            return True       