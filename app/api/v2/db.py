import os
import psycopg2
from instance.config import app_config
# env = os.environ['ENV']

# url = app_config[env].DATABASE_URI
# # print(url)

url = "postgres://admin:admin123@localhost:5432/politico"


def connection(url):
    """This function creates a connection to the database"""
    return psycopg2.connect(url)


def db():
    """This function returns a database connection object"""
    return connection(url)


def create_tables():
    """This function creates tables in the database"""
    conn = connection(url)
    cursor = conn.cursor()
    queries = create_queries()
    for query in queries:
        cursor.execute(query)
    conn.commit()


def destroy_tables():
    """This function destroys tables in the database"""
    conn = connection(url)
    cursor = conn.cursor()
    statements = destroy_queries()
    for statement in statements:
        cursor.execute(statement)
    conn.commit()


def destroy_queries():
    """This function returns a list of 'destroy table' queries"""
    delete_users = """DROP TABLE IF EXISTS users;"""
    delete_parties = """DROP TABLE IF EXISTS parties;"""
    delete_offices = """DROP TABLE IF EXISTS offices;"""
    delete_blacklist = """DROP TABLE IF EXISTS blacklist;"""
    delete_candidates = """DROP TABLE IF EXISTS candidates;"""
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

    blacklist = """CREATE TABLE IF NOT EXISTS blacklists(
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
               blacklist, candidates, votes, petitions]

    return queries
