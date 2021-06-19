import connexion
import six

from werkzeug.security import generate_password_hash, check_password_hash
from flask import abort, request, Response

from jobbing.DBModels import User as DBUser
from jobbing.models.user import User  # noqa: E501
from jobbing import util


def login():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        return '', 401

    return 'logged in', 200

def logout():
    return 'logged out'

def get_user_by_id(uid):  # noqa: E501
    """get_user_by_id

    Displays a User defined by ID # noqa: E501

    :param uid: Unique identifier
    :type uid: str

    :rtype: User
    """
    user = DBUser.query.filter(DBUser.uid == uid).first()

    if user == None:
        abort(404)
    return User(user_id=user.id, uid=user.uid, username=user.username, email=user.email, image_profile=user.image_profile, role_id=user.role_id)

def get_users():  # noqa: E501
    """get_users

    Lists all users # noqa: E501


    :rtype: User
    """
    users = DBUser.query.all()
    results = [
        User(user_id=user.id, uid=user.uid, username=user.username, email=user.email, image_profile=user.image_profile, role_id=user.role_id) for user in users]
    return results


def save_user(body):  # noqa: E501
    """save_user

    Creates a user # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
