from sqlalchemy_wrapper import SQLAlchemy

db = SQLAlchemy(uri="sqlite:///my_db.db")
Model = db.Model
