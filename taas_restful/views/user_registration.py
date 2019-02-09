from taas_restful.models.user import User
from taas_restful.utils.custom_exceptions import ResourceAlreadyPresent


def user_registration(data):
    try:
        User.insert_user(data)
    except:
        raise ResourceAlreadyPresent("User already exists with this email address")