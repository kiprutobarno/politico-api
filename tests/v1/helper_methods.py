from flask import current_app

# Party test methods

def create_party(self, data):
    """Create party endpoint test method """
    return self.client.post(
        'api/v1/parties',
        data=data,
        content_type='application/json'
    )

def get_all_parties(self):
    """Get all parties endpoint test method """
    return self.client.get(
        '/api/v1/parties',
        content_type='application/json'
    )

def get_specific_party(self):
    """Get specific party endpoint test method """
    return self.client.get(
        '/api/v1/parties/1',
        content_type='application/json'
    )

def edit_party(self, data):
    """Edit political party endpoint test method """
    return self.client.patch(
        '/api/v1/parties/1/Red',
        data=data,
        content_type='application/json'
    )

def delete_party(self):
    return self.client.delete(
        '/api/v1/parties/1',
        content_type='application/json',
    )


# Office test methods

def create_office(self, data):
    """Create office endpoint test method """
    return self.client.post(
        'api/v1/offices',
        data=data,
        content_type='application/json'
    )

def get_all_offices(self):
    """Get all offices endpoint test method """
    return self.client.get(
        '/api/v1/offices',
        content_type='application/json'
    )

def get_specific_office(self):
    """Get specific office endpoint test method """
    return self.client.get(
        '/api/v1/offices/1',
        content_type='application/json'
    )