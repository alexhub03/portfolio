from flask_sqlalchemy import SQLAlchemy
 
db =SQLAlchemy()
 
class GuestsModel(db.Model):
    __tablename__ = "table"
 
    id = db.Column(db.Integer, primary_key=True)
    guest_id = db.Column(db.Integer(),unique = True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    email = db.Column(db.String(80))
 
    def __init__(self, guest_id,name,age,email):
        self.guest_id = guest_id
        self.name = name
        self.age = age
        self.email = email
 
    def __repr__(self):
        return f"{self.name}:{self.guest_id}"


