from flask import current_app as app, Config
from sqlalchemy_wrapper import SQLAlchemy

config_name = 'taas_restful.settings.Config'
config = Config("")
config.from_object(config_name)

db = SQLAlchemy(uri=config['DATABASE_URL'])
Model = db.Model