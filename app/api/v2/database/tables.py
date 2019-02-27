def destroy_queries():
    """This function returns a list of 'destroy table' queries"""
    delete_users = """DROP TABLE IF EXISTS users CASCADE;"""
    delete_parties = """DROP TABLE IF EXISTS parties CASCADE;"""
    delete_offices = """DROP TABLE IF EXISTS offices CASCADE;"""
    delete_candidates = """DROP TABLE IF EXISTS candidates CASCADE;"""
    delete_votes = """DROP TABLE IF EXISTS votes;"""
    delete_petitions = """DROP TABLE IF EXISTS petitions;"""

    statements = [
        delete_candidates,
        delete_votes,
        delete_petitions,
        delete_users,
        delete_parties,
        delete_offices]
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
                    FOREIGN KEY(candidate) REFERENCES users(id)
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

    queries = [users, parties, offices, candidates, votes, petitions]

    return queries
