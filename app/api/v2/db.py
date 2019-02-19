import os
import psycopg2
from instance.config import app_config
from flask import current_app

def connection():
    """This function creates a connection to the database"""
    if current_app.config['TESTING']:
        url=os.getenv('TEST_DATABASE')
    else:
        url=os.getenv('DATABASE')
    return psycopg2.connect(url)

def db():
    """This function returns a database connection object"""
    return connection()


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


def destroy_queries():
    """This function returns a list of 'destroy table' queries"""
    delete_users = """DROP TABLE IF EXISTS users CASCADE;"""
    delete_parties = """DROP TABLE IF EXISTS parties CASCADE;"""
    delete_offices = """DROP TABLE IF EXISTS offices CASCADE;"""
    delete_blacklist = """DROP TABLE IF EXISTS blacklists CASCADE;"""
    delete_candidates = """DROP TABLE IF EXISTS candidates CASCADE;"""
    delete_votes = """DROP TABLE IF EXISTS votes;"""
    delete_petitions = """DROP TABLE IF EXISTS petitions;"""

    statements = [delete_candidates, delete_votes, delete_petitions,
                  delete_blacklist, delete_users, delete_parties, delete_offices]
    return statements


def create_queries():
    """This function returns a list of 'create table' queries"""
    users = """CREATE TABLE IF NOT EXISTS users(
                    id SERIAL PRIMARY KEY NOT NULL, 
                    firstName VARCHAR(50) NOT NULL,
                    lastName VARCHAR(50) NOT NULL,
                    otherName VARCHAR(50) NOT NULL,
                    email VARCHAR(50) NOT NULL,
                    phoneNumber VARCHAR(50) NOT NULL,
                    passportUrl VARCHAR(50) NOT NULL,
                    isAdmin BOOLEAN DEFAULT FALSE,
                    isCandidate BOOLEAN DEFAULT FALSE,
                    password VARCHAR(200) NOT NULL,
                    dateCreated TIMESTAMP NULL DEFAULT NOW() );"""

    parties = """CREATE TABLE IF NOT EXISTS parties(
                    id SERIAL PRIMARY KEY NOT NULL, 
                    name VARCHAR(50) NOT NULL,
                    hqAddress VARCHAR(50) NOT NULL,
                    logoUrl VARCHAR(50) NOT NULL );"""

    offices = """CREATE TABLE IF NOT EXISTS offices(
                    id SERIAL PRIMARY KEY NOT NULL, 
                    type VARCHAR(50) NOT NULL,
                    name VARCHAR(50) NOT NULL );"""

    blacklists = """CREATE TABLE IF NOT EXISTS blacklists(
                    id SERIAL PRIMARY KEY NOT NULL, 
                    token VARCHAR(500) NOT NULL,
                    token_type VARCHAR(50) NOT NULL,
                    admin VARCHAR(50) NOT NULL,
                    issued_at VARCHAR(50) NOT NULL,
                    expires_at VARCHAR(50) NOT NULL,
                    blacklisted_at TIMESTAMP NULL DEFAULT NOW() );"""

    candidates = """CREATE TABLE IF NOT EXISTS candidates(
                    id SERIAL PRIMARY KEY NOT NULL, 
                    office INTEGER NOT NULL, 
                    party INTEGER NOT NULL, 
                    candidate INTEGER NOT NULL,
                    dateCreated TIMESTAMP NULL DEFAULT NOW(),
                    FOREIGN KEY(office) REFERENCES offices(id),
                    FOREIGN KEY(party) REFERENCES parties(id),
                    FOREIGN KEY(candidate) REFERENCES users(id)
                    ON DELETE CASCADE ON UPDATE CASCADE );"""

    votes = """CREATE TABLE IF NOT EXISTS votes(
                    id SERIAL PRIMARY KEY NOT NULL, 
                    createdOn TIMESTAMP NULL DEFAULT NOW(),
                    createdBy INTEGER NOT NULL,
                    office INTEGER NOT NULL, 
                    candidate INTEGER NOT NULL,
                    FOREIGN KEY(office) REFERENCES offices(id),
                    FOREIGN KEY(candidate) REFERENCES candidates(id)
                    ON DELETE CASCADE ON UPDATE CASCADE );"""

    petitions = """CREATE TABLE IF NOT EXISTS petitions(
                    id SERIAL PRIMARY KEY NOT NULL, 
                    createdOn TIMESTAMP NULL DEFAULT NOW(),
                    createdBy INTEGER NOT NULL,
                    office INTEGER NOT NULL,
                    body VARCHAR(500) NOT NULL,
                    FOREIGN KEY(createdBy) REFERENCES users(id),
                    FOREIGN KEY(office) REFERENCES offices(id)
                    ON DELETE CASCADE ON UPDATE CASCADE );"""

    queries = [users, parties, offices,
               blacklists, candidates, votes, petitions]

    return queries


def default_admin():
    conn = connection()
    curr = conn.cursor()
    query = """SELECT * FROM users WHERE email='admin@politico.com'"""
    curr.execute(query)
    admin = curr.fetchone()
    if not admin:
        query = """INSERT INTO users(firstName, lastName, otherName, email, phoneNumber, passportUrl, isadmin, password) VALUES(%s,%s,%s,%s,%s, %s,%s,%s)"""

        curr.execute(query, ('Kipruto','Barno', 'Maxwel', 'admin@politico.com', '0721884344', 'admin.png', True, '$pbkdf2-sha256$29000$ndPaWwsBICREiPG.FyLkvA$HZhdbbXke3brKlrPxaGve/uqfwHpM0WhaaPIJu5fPLY'))
        conn.commit()

