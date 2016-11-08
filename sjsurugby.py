import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, send_file

# create our little application :)
app = Flask(__name__)

DATABASE = '/Users/jianganson72/Desktop/sjsurugbywebsite/sjsurugby.db'

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/")
def index():
    return redirect(url_for('home'))

@app.route("/roster")
def roster():
    con = sqlite3.connect("sjsurugby.db")
    print "Opened database successfully"
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("Select * FROM roster order by Name asc")

    roster = cur.fetchall()

    con.commit()
    con.close()
    return render_template("roster.html", roster = roster)

@app.route("/contact")
def contact():
    con = sqlite3.connect("sjsurugby.db")
    print "Opened database successfully"
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("Select * from contact")

    contact = cur.fetchall()

    con.commit()
    con.close()
    return render_template("contact.html", contact = contact)

@app.route("/location")
def location():
    return render_template("location.html")

@app.route("/information")
def information():
    return render_template("information.html")

@app.route("/media")
def media():
    return render_template("media.html")

@app.route("/schedule")
def schedule():
    con = sqlite3.connect("sjsurugby.db")
    print "Opened database successfully"
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("Select * FROM schedule")

    schedule = cur.fetchall()

    con.commit()
    con.close()
    return render_template("schedule.html", schedule = schedule)

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv



if __name__ == "__main__":
	app.run();