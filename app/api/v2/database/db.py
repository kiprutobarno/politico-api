import os
import psycopg2
from flask import current_app
from app.api.v2.database.tables import create_queries, destroy_queries


def connection():
    """This function creates a connection to the database"""
    if current_app.config['TESTING']:
        URL = os.getenv('TEST_DATABASE_URL')
    else:
        URL = os.getenv('DATABASE_URL')
    return psycopg2.connect(URL)


def create_tables():
    """This function creates tables in the database"""
    conn = connection()
    cursor = conn.cursor()
    queries = create_queries()
    for query in queries:
        cursor.execute(query)
    conn.commit()


def destroy_tables():
    """This function destroys tables in the database"""
    conn = connection()
    cursor = conn.cursor()
    statements = destroy_queries()
    for statement in statements:
        cursor.execute(statement)
    conn.commit()


def drop(table):
    connection.cursor.execute(
        "DROP TABLE IF IT EXISTS {} CASCADE;".format(table))
    value = connection.commit()
    return value


def insert(table, data):
    """ insert data """
    keys = ', '.join([key for key in data])
    values = str(tuple([data[key] for key in data]))
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(
        """ INSERT INTO {}({}) VALUES {} """.format(table, keys, values))
    value = conn.commit()
    return value


def fetch_all_items(table):
    """ Fetch all items """
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM {}""".format(table))
    items = cursor.fetchall()
    return items


def fetch_single_item(table, id):
    """ Fetch single item """
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT * FROM {} WHERE {} = {}""".format(table, id, id))
    item = cursor.fetchall()
    return item


def fetch_item_multiple_conditions(table, parameter1, parameter2):
    """ Get specific item """
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT * FROM {} WHERE {} = {} and {} = {}""".format(table, parameter1, parameter1, parameter2, parameter2))
    item = cursor.fetchall()
    return item


def search_by_name(table, name):
    """ Search specific item """
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT * FROM {} WHERE name='%s'""".format(table) % (name))
    item = cursor.fetchall()
    return item


def search_by_email(table, email):
    """ Search specific item """
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT * FROM {} WHERE email='%s'""".format(table) % (email))
    item = cursor.fetchone()
    return item


def delete(table, id):
    """ Delete a specific item from table """
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(
        """DELETE FROM {} WHERE id = {}""".format(table, id))
    return conn.commit()


def fetch_candidate(selector, value):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(""" SELECT users.firstname, users.lastname, offices.name, parties.name
                    FROM candidates INNER JOIN users ON candidates.candidate=users.id
                    INNER JOIN offices ON candidates.office=offices.id
                    INNER JOIN parties ON candidates.party=parties.id WHERE {}={}""".format(selector, value))
    item = cursor.fetchone()
    return item


def fetch_all_candidates(selector, value):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(""" SELECT users.firstname, users.lastname, offices.name, parties.name
                    FROM candidates INNER JOIN users ON candidates.candidate=users.id
                    INNER JOIN offices ON candidates.office=offices.id
                    INNER JOIN parties ON candidates.party=parties.id WHERE {}={}""".format(selector, value))
    item = cursor.fetchall()
    return item


def fetch_all_results(id):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT offices.name, users.firstname, users.lastname, COUNT(*) as votes FROM votes
                   INNER JOIN offices ON offices.id=votes.office
                   INNER JOIN users ON users.id=votes.candidate WHERE office={}
                   GROUP BY offices.name, users.firstname, users.lastname;""".format(id))
    item = cursor.fetchall()
    return item


def default_admin():
    admin = {
        "firstName": "Kipruto",
        "lastName": "Barno",
        "otherName": "Maxwel",
        "email": "admin@politico.com",
        "phoneNumber": "0708344488",
        "passportUrl": "admin.png",
        "isAdmin": True,
        "password": "$pbkdf2-sha256$29000$gvC.1/q/9x7DGKP0fu/dWw$k5fSiU1MK/XHyMbZofnBxrE.OPd.FScTNntfJGwnt48"
    }
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT * FROM users WHERE email='admin@politico.com'""")
    if not cursor.fetchone():
        insert('users', admin)
