from app.api.v2.database.db import Connection


class Result:
    """ The candidate model """

    def __init__(self):
        self.db = Connection()

    def get(self, id):
        data = self.db.fetch_all_results(id)
        rows = []
        for i, items in enumerate(data):
            office, firstname, lastname, othername, party, results, = items
            result = dict(
                office=office,
                candidate=firstname,
                lastname=lastname,
                othername=othername,
                party=party,
                results=results
            )
            rows.append(result)

        return rows

    def search(self, office):
        """ This function returns True if an office was available for election"""
        if self.db.fetch_single_item('offices', office):
            return True
