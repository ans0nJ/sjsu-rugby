import sqlite3
from flask import Flask, g, render_template
from flask_sqlalchemy import SQLAlchemy
from app.config import DATABASE


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app.views import home

def create_app():
    return app
