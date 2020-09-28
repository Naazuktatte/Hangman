from flask import Flask, render_template, request
import os
import re
import requests
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

#************************************************************
# Python App name, config attachment to app name
hangman = Flask(__name__)
hangman.config.from_object(os.environ['APP_SETTINGS'])
hangman.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#************************************************************
# Creating db handler for migration/upgrade, db engine for ORM, session created for ORM, binding engine to session
# Creating base declarative class for creating table 
#the db handler for migrations n stuff
hangmanDb = SQLAlchemy(hangman)
# hangman db engine for ORM
hangmanDbEngine = create_engine(os.environ['DATABASE_URL'])
# hangman db ORM session
hangmanDbSession = sessionmaker()
hangmanDbSession.configure(bind=hangmanDbEngine)


# function to be called for welcome
@hangman.route('/hangman')
def welcome():
    return render_template('index.html', title="Hangman Game (through flask)")

# function to be called when click on submit, check index.html form
@hangman.route('/hangman/login', methods=["POST"])
def login():
    logUserName = request.form["login_username"]
    logPassword = request.form["login_password"]



if __name__ == '__main__':
    hangman.run(debug=True,host='0.0.0.0', port=4000)