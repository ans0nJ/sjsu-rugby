import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, send_file

app = Flask(__name__)

DATABASE = '/Users/jianganson72/Desktop/sjsu-rugby/sjsurugby.db'

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

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sjsurugby'):
        g.sqlite_db.close()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/schedule/")
def schedule():
    db = get_db()
    cur = db.execute("Select * FROM schedule")
    schedule = cur.fetchall()
    return render_template("schedule.html", schedule = schedule)

@app.route("/roster/")
def roster():
    db = get_db()
    cur = db.execute("SELECT * FROM roster ORDER BY Name ASC")
    roster = cur.fetchall()
    return render_template("roster.html", roster = roster)

@app.route("/contact/")
def contact():
    db = get_db()
    cur = db.execute("SELECT * FROM contact")
    contact = cur.fetchall()
    return render_template("contact.html", contact = contact)

if __name__ == "__main__":
	app.run();