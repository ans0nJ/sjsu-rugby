import sqlite3
from flask import Flask, g, render_template
from db import get_db

app = Flask(__name__)


def create_app():

    @app.teardown_appcontext
    def close_db(error):
        """Closes the database again at the end of the request."""
        if hasattr(g, 'sjsurugby'):
            g.sqlite_db.close()

    @app.route("/")
    def home():
        db = get_db()
        cur = db.execute("SELECT * FROM schedule")
        schedule = cur.fetchall()
        cur = db.execute("SELECT * FROM roster ORDER BY Name ASC")
        roster = cur.fetchall()
        return render_template("index.html", schedule=schedule, roster = roster)

    @app.route("/#schedule/")
    def schedule():
        db = get_db()
        cur = db.execute("SELECT * FROM schedule")
        schedule = cur.fetchall()
        return render_template("index.html", schedule=schedule)

    @app.route("/roster/")
    def roster():
        db = get_db()
        cur = db.execute("SELECT * FROM roster ORDER BY Name ASC")
        roster = cur.fetchall()
        return render_template("roster.html", roster=roster)

    @app.route("/contact/")
    def contact():
        db = get_db()
        cur = db.execute("SELECT * FROM contact")
        contact = cur.fetchall()
        return render_template("contact.html", contact=contact)

    return app
