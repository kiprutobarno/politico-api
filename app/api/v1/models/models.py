parties = []
offices = []

class Party:
    """ The party model """
    def __init__(self):
        self.parties=parties

    def create_party(self, name, hqAddress, logoUrl):
        """ Create a party method """
        party = {
            "id": len(parties)+1,
            "name": name,
            "hqAddress": hqAddress,
            "logoUrl": logoUrl
        }
        
        self.parties.append(party)
        return party

    def get_all_parties(self):
        """ Get all parties method """
        return self.parties

    def get_specific_party(self, id):
        """ Get specific party method """
        for party in self.parties:
            if party['id'] == id:
                return party

    def edit_party(self, id, name, data):
        """Update the details of a political party"""
        for party in self.parties:
            if party['id'] == id and party['name'] == name:
                if data.get('name'):
                    party['name'] = data.get('name')

                if data.get('hqAddress'):
                    party['hqAddress'] = data.get('hqAddress')
                if data.get('logoUrl'):
                    party['logoUrl'] = data.get('logoUrl')
                return party

    def delete_party(self, id):
        """ Delete party method """
        for party in self.parties:
            if party['id'] == id:
                return self.parties.remove(party)


class Office:
    """The Office model"""

    def __init__(self):
        self.offices = offices

    
    def create_office(self, office_type, name):
        """ Create a office method """
        office = {
            "id": len(self.offices)+1,
            "type": office_type,
            "name": name
        }
        self.offices.append(office)
        return office

    def get_all_offices(self):
        """ Get all offices method """
        return self.offices

    def get_specific_office(self, id):
        """ Get specific office method """
        for office in self.offices:
            if office['id'] == id:
                return office