# coding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_oauthlib.provider import OAuth2Provider


app = Flask(__name__, template_folder='templates')
app.debug = True
app.secret_key = 'secret'
app.config.update({
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///db.sqlite',
})
db = SQLAlchemy(app)
oauth = OAuth2Provider(app)