from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Books(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30),unique=True, nullable = False)
    company = db.Column(db.String(60), nullable = False)

    def __init__(self, name, company):
        self.name = name
        self.company = company
