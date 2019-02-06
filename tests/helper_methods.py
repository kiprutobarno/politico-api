from flask import current_app

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
        '/api/v1/parties/1',
        data=data,
        content_type='application/json'
    )