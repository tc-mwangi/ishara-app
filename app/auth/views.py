from . import auth
from .. import db


@auth.route('/')
def login():
    return '<h1> This is the login page </h1>'
