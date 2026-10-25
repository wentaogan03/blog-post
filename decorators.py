from flask_login import current_user
from flask import abort
from functools import wraps

def admin_only(function):

    @wraps(function)
    def wrapper_function(*args, **kwargs):
        print(current_user.id)
        if current_user.is_authenticated and current_user.id == 1:
            return function(*args, **kwargs)
        return abort(403)
    return wrapper_function