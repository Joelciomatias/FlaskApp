from flask_sqlalchemy import SQLAlchemy
from  . import app
db = SQLAlchemy(app)

class TestPython(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    sum = db.Column('sum',db.Float())
    start = db.Column('start',db.DateTime())
    end = db.Column('end',db.DateTime())
    iterations = db.Column('iterations', db.Integer)