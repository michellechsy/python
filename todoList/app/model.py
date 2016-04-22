import web

from todoList import *

db = web.database(dbn=DB_DBN, db=DB_SCHEMA,
                  user=DB_USER, pw=DB_PASSWD,
                  host=DB_HOST)

TODO_TABLE = 'todo'


def get_todos():
    return db.select(TODO_TABLE, order='id')


def new_todo(text):
    db.insert(TODO_TABLE, title=text)


def del_todo(id):
    db.delete(TODO_TABLE, where="id=$id", vars=locals())
