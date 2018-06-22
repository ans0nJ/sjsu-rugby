from flask import Flask
from app import db
from flask_sqlalchemy import SQLAlchemy


class Schedule(db.Model):
    __tablename__ = 'schedule'
    date = db.Column(db.String(128), primary_key=True)
    team = db.Column(db.String(128))
    location = db.Column(db.String(128))
    time = db.Column(db.String(128))
    score = db.Column(db.String(128))

    def __repr__(self):
        return
        "<Schedule(date='%s', team='%s', location='%s', time='%s',"
        + "score='%s')>" % (self.date, self.team,
                            self.location, self.time, self.score)


class Roster(db.Model):
    __tablename__ = 'roster'
    name = db.Column(db.String(128), primary_key=True)
    position = db.Column(db.String(128))
    height = db.Column(db.String(128))
    weight = db.Column(db.String(128))
    year = db.Column(db.String(128))
    hometown = db.Column(db.String(128))

    def __repr__(self):
        return
        "<Roster(name='%s', position='%s', height='%s', weight='%s', "
        + "year='%s', hometown='%s')>" % (
                                        self.name, self.position, self.height,
                                        self.weight, self.year, self.hometown)


class Contact(db.Model):
    __tablename__ = 'contact'
    name = db.Column(db.String(128), primary_key=True)
    position = db.Column(db.String(128))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(128))

    def __repr__(self):
        return "<Contact(name='%s', position='%s', email='%s', "
        + "phone='%s')>" % (self.name, self.position, self.email, self.phone)
