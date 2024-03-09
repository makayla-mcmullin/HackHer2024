
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
    
    companionship = db.Column(db.TinyInt, unique=False, nullable=True)
    grocery = db.Column(db.TinyInt, unique=False, nullable=True)
    cleaning = db.Column(db.TinyInt, unique=False, nullable=True)
    transportation = db.Column(db.TinyInt, unique=False, nullable=True)
    
    matches = db.relationship('matches', backref='ElderUser')

    

class HelperUser(db.Model):
   """This class initializes the ElderUser data base"""
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(80), unique=True, nullable=False)
   email = db.Column(db.String(120), unique=True, nullable=False)
   password = db.Column(db.String(80), unique=True, nullable=False)
   location = db.Column(db.String(80), unique=True, nullable=False)
   
   companionship = db.Column(db.TinyInt, unique=False, nullable=True)
   grocery = db.Column(db.TinyInt, unique=False, nullable=True)
   cleaning = db.Column(db.TinyInt, unique=False, nullable=True)
   transportation = db.Column(db.TinyInt, unique=False, nullable=True)
   
   matches = db.relationship('matches', backref='HelperUser')

   

class Matches(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    helper_id = db.Column(db.Integer, db.ForeignKey('HelperUser.id'))
    elder_id= db.Column(db.Integer, db.ForeignKey('ElderUser.id'))

db.create_all()



