from flask import current_app

def create_party(self, data):
    return self.client.post(
        'api/v1/parties',
        data=data,
        content_type='application/json'
    )

def get_all_parties(self):
    return self.client.get(
        '/api/v1/parties',
        content_type='application/json'
    )

def get_specific_party(self):
    return self.client.get(
        '/api/v1/parties/1',
        content_type='application/json'
    )