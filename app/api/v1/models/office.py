offices = []

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