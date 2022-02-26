from functools import wraps
from flask import session, redirect
       

def login_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def error(errorCode, ErrorMessage):
    '''
    Return a Dictionary
    with the keys as Code and Message and Status
    '''
    d={}
    d['code'] = errorCode
    d['message'] = str(ErrorMessage)
    d['status'] = 'Failed'

    return d
