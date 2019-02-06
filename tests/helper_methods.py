from flask import current_app

def create_party(self, data):
    return self.client.post(
        'api/v1/parties',
        data=data,
        content_type='application/json'
    )