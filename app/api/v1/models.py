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