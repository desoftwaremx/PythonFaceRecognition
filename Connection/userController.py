from .Controller.connection import db
from .Controller.read import ReadUser
from .Controller.insert import InsertUser
from .Controller.delete import DeleteUser
from .Controller.edit import EditUser

def check_connections():
    result = 0;
    try:
        try:
            db
            print("connection Success")
            result = 1
        except (RuntimeError, TypeError, NameError):
            print('something happened')
    finally:
        return result

def read_user():
    return ReadUser()

def insert_user():
    return InsertUser()

def update_user():
    return EditUser(int(input("Enter Id to update : ")))

def delete_user():
    return DeleteUser(int(input("Enter Id to update : ")))

check_connections()
