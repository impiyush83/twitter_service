from sqlalchemy import String

from taas_restful.models.db import Model, db
from taas_restful.utils.helper import encrypt_password


class User(Model):

    email = db.Column(String(256), primary_key=True)
    password = db.Column(String(256), nullable=False)

    consumer_key = db.Column(String(256), nullable=False)
    consumer_secret = db.Column(String(256), nullable=False)
    access_token = db.Column(String(256), nullable=False)
    access_token_secret = db.Column(String(256), nullable=False)

    @classmethod
    def insert_user(cls, user_obj):
        encrypted_password = encrypt_password(user_obj.get("password"))
        u1 = cls(email=user_obj.get("email"), password=encrypted_password,
                 consumer_key=user_obj.get("consumer_key"), consumer_secret=user_obj.get("consumer_secret_key"),
                 access_token=user_obj.get("access_token"), access_token_secret=user_obj.get("access_secret_token"))
        db.session.add(u1)
        db.flush()

    @classmethod
    def with_email(cls, email):
        return db.query(User).filter(User.email == email).first()


db.create_all()
