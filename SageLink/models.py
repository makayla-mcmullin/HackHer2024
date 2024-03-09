
from datetime import date
from SageLink import app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# # ^ need to decide what database we connect to?
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class ElderUser(db.Model):
    """This class initializes the ElderUser data base"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    location = db.Column(db.String(80), unique=True, nullable=False)


    matches = db.relationship('matches', backref='user')

    #transaction = db.relationship('transaction', backref='user')

    # Make relationship with listings and booking databases
    # TODO: ensure listing and booking databases have corresponding code

class HelperUser(db.Model):
   """This class initializes the ElderUser data base"""
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(80), unique=True, nullable=False)
   email = db.Column(db.String(120), unique=True, nullable=False)
   password = db.Column(db.String(80), unique=True, nullable=False)
   location = db.Column(db.String(80), unique=True, nullable=False)

class Matches(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    helper_id = db.Column(db.Integer, db.ForeignKey('HelperUser.id'))
    elder_id= db.Column(db.Integer, db.ForeignKey('ElderUser.id'))

db.create_all()



    
# def login(email, password):
#     """
#     This function validates username and password before login is
#     completed.

#     Parameters:
#         username (string): user name
#         password (string): user password
#     """
    

#     if verify_password(password) and verify_email(email):
#         result = User.query. \
#             filter_by(email=email, password=password).all()

#         # check to see if the search got precisely one result
#         if len(result) != 1:
#             print("User not found, maybe try to register first?")
#             return None
#         else:
#             print("Login successful! Welcome back, " + email + "!")
#             return result[0]

# def register(username, email, password):
#     """
#     Register a new user
#       Parameters:
#         username (string):     user name
#         email (string):    user email
#         password (string): user password
#       Returns:
#         True if registration succeeded otherwise False

#     """

#     if validate_username(username) == True:  # username vaild (r1-5, r1-6)
#         if verify_password(password) == True:  # password vaild (r1-4)
#             if verify_email(email) == True:  # email vaild (r1-3)
#                 # check if the email has been used: (r1-7)
#                 existed = User.query.filter_by(email=email).all()
#                 if len(existed) > 0:
#                     return False

#                 # create a new user
#                 user = User(username=username, email=email, password=password,
#                             billing_address=" ", postal_code=" ", balance=100)
#                 # add it to the current database session
#                 db.session.add(user)
#                 # actually save the user object
#                 db.session.commit()
#                 return True

#     return False


# def verify_email(email):
#     """
#     This function is used in the register and update_email functions to
#     check that a given email is valid under RFC 5322 specifications.
#     parameter: an email address
#     return: boolean variable True if email address is vaild and False
#             if not valid.
#     """

#     if len(email) != 0:
#         try:
#             valid_email = validate_email(email).email
#             email = valid_email["email"]
#             return True
#         except:
#             return False


# def verify_password(password):
#     """
#     This function is used in the register and login functions to check
#     that a given password is vaild
#     parameter: password
#     return: boolean variable True if password is vaild and False if
#             not valid.
#     """

#     caps_check = 0
#     lower_check = 0
#     num_check = 0
#     special_check = 0

#     for char in password:
#         if char.isupper():
#             caps_check += 1
#         elif char.islower():
#             lower_check += 1
#         elif char.isnumeric():
#             num_check += 1
#         elif not char.isalnum():
#             special_check += 1

#     if (len(password) >= 6 and caps_check >= 1 and
#             lower_check >= 1 and num_check >= 1 and special_check >= 1):
#         return True
#     else:
#         return False


# def validate_username(username):
#     """
#     :return: A boolean that determines if the username is valid or not
#     """
#     # This function serves to satisfy requirements R1-5 and R1-6
#     if username != "" and username.isalnum() \
#             and not (username.find(" ") == 0 or
#                      username.find(" ") == len(username)):
#         return True
#     else:
#         return False
