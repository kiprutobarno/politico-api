parties = []

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