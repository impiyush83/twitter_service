from flask import jsonify
from flask_jwt_extended import create_access_token
from taas_restful.models.models import User
from taas_restful.utils.customer_exceptions import NoResultFound
from taas_restful.utils.helper import check_encrypted_password


def user_login(data):
    # get parser data
    # get user from database
    user = User.with_email(data.get("email"))
    wrong_password = 'Password is wrong.'
    if user is None:
        raise NoResultFound("User not found")

    if not check_encrypted_password(data['password'], user.password):
        return jsonify({'message': wrong_password}), 401
    # if correct user password

    # create access token
    access_token = create_access_token(identity=user.email)

    # refresh_token = create_refresh_token(user.id)
    return access_token, user

