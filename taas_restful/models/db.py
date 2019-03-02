import os

from flask import Config
from sqlalchemy_wrapper import SQLAlchemy

config_name = 'taas_restful.settings.Config'
config = Config("")
config.from_object(config_name)

db = SQLAlchemy(uri=os.environ.get('DATABASE_URL'))
Model = db.Model
