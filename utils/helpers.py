from functools import wraps
from utils.validations import error
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    verify_jwt_in_request,
    get_jwt_claims,)

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        jwt_holder()
        if get_jwt_claims()['isAdmin'] != True:
            return error(403, "Admin rights required!")
            pass
        return fn(*args, **kwargs)
    return wrapper

def jwt_holder():
    return verify_jwt_in_request()


def drop(table):
    return "DROP TABLE IF IT EXISTS {} CASCADE;".format(table)

def insert(table, data):
        """ insert data """
        keys = ', '.join([key for key in data])
        values = str(tuple([data[key] for key in data]))
        return """ INSERT INTO {}({}) VALUES {} """.format(table, keys, values)

def update(table, data, id):
        """ update data """
        keys = [key for key in data]
        values = ', '.join(str(tuple([data[key] for key in data])))
        return """ UPDATE {} SET {} = {} WHERE {} = {} """.format(table, data, id)

        # "UPDATE parties SET name=%s, hqAddress=%s, logoUrl=%s WHERE id={}"
 

def get_all(table):
        """ Get all items """
        return """SELECT * FROM {}""".format(table)

def get_one(table, id):
        """ Get specific item """
        return """SELECT * FROM {} WHERE id = {}""".format(table, id)

def search(table, parameter):
        """ Get specific item """
        return """SELECT * FROM {} WHERE name='%s'""".format(table) % (parameter)
        

def delete(table, id):
        """ Get specific item """
        return """DELETE FROM {} WHERE id = {}""".format(table, id)


allowed_offices = ['Presidential', 'Gubernatorial', 'Senatorial']
allowed_office_types = ['National', 'County']