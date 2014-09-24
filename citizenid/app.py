# coding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_oauthlib.provider import OAuth2Provider

from citizenid import default_settings

app = Flask(__name__)

app.config.from_object(default_settings)
app.config.from_envvar('COAF_SETTINGS', silent=True)

db = SQLAlchemy(app)
oauth = OAuth2Provider(app)
