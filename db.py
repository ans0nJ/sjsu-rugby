import sqlite3
from flask import Flask, g, render_template
from config import DATABASE


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(DATABASE)
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sjsurugby'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
