from app.api.v2.database.db import search_by_name, fetch_all_results, fetch_single_item


class Result:
    """ The candidate model """

    def get(self, id):
        data = fetch_all_results(id)
        rows = []
        for i, items in enumerate(data):
            office, firstname, lastname, results = items
            result = dict(
                office=office,
                candidate=firstname+" "+lastname,
                results=results
            )
            rows.append(result)

        return rows

    def search(self, office):
        """ This function returns True if an office is available for election"""
        data = fetch_single_item('offices', office)
        if len(data) > 0:
            return True
