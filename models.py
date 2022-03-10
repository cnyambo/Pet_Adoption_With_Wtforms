from email.policy import default
from enum import unique
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, delete, desc,   func, null


#initialize sqlAlchemy

db =SQLAlchemy()
#connect app to db instance
def connectdb(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet table creation"""
    __tablename__ ='pets'

    id= db.Column(db.Integer, primary_key = True, autoincrement =True)    
    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    photo_url = db.Column(db.Text, nullable=True)
    age=db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean)

    @classmethod
    def add_new_pet(cls, name, species, photo_url, age,notes,available):
        new_pet = Pet(name = name, species=species, photo_url=photo_url, age=age,notes=notes,available=available)
        db.session.add(new_pet)
        db.session.commit()  