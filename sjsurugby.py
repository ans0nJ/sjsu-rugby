import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

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

if __name__ == "__main__":
	app.run();