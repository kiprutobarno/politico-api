from app.api.v2.database.db import Connection


class Nomination:
    """Self nomination model"""

    def __init__(self):
        self.db = Connection()

    def expressInterest(self, user, party, office):
        interest = {
            "usr": user,
            "party": party,
            "office": office
        }

        self.db.insert('nominations', interest)
        return interest

    def alreadyExpressed(self, usr):
        if self.db.fetch_single_item('nominations', usr):
            return True
