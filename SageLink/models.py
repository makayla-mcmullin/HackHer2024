
from datetime import date
from SageLink import app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship


db = SQLAlchemy(app)


class ElderUser(db.Model):
    """This class initializes the ElderUser data base"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    location = db.Column(db.String(80), unique=True, nullable=False)
    
    companionship = db.Column(db.Boolean, unique=False, nullable=True)
    grocery = db.Column(db.Boolean, unique=False, nullable=True)
    cleaning = db.Column(db.Boolean, unique=False, nullable=True)
    transportation = db.Column(db.Boolean, unique=False, nullable=True)
    
    matches = db.relationship('Matches', backref='elder_user')

    

class HelperUser(db.Model):
   """This class initializes the ElderUser data base"""
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(80), unique=True, nullable=False)
   email = db.Column(db.String(120), unique=True, nullable=False)
   password = db.Column(db.String(80), unique=True, nullable=False)
   location = db.Column(db.String(80), unique=True, nullable=False)
   
   companionship = db.Column(db.Boolean, unique=False, nullable=True)
   grocery = db.Column(db.Boolean, unique=False, nullable=True)
   cleaning = db.Column(db.Boolean, unique=False, nullable=True)
   transportation = db.Column(db.Boolean, unique=False, nullable=True)
   
   matches = db.relationship('Matches', backref='helper_user')

   

class Matches(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    helper_user_id = db.Column(db.Integer, db.ForeignKey('helper_user.id'))
    elder_user_id= db.Column(db.Integer, db.ForeignKey('elder_user.id'))

db.create_all()



