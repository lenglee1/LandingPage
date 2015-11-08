from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash


db = SQLAlchemy()



class Pref(db.Model):
	__tablename__ = 'prefs'
	uid = db.Column(db.Integer, primary_key = True)
	bio = db.Column(db.Text, unique = True, index = True)
	food_choice = db.Column(db.String(64))
	employment_status = db.Column(db.String(64)) 

	def __repr__(self):
		return '<User {0}>'.format(self.username)


class User(db.Model):
	__tablename__ = 'users'
	uid = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(120), unique=True)
	username = db.Column(db.String(64))
	pwdhash = db.Column(db.String(54))

	def __init__(self, email, username, password):
		self.email = email
		self.username = username
		self.set_password(password)

	def set_password(self, password):
		self.pwdhash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.pwdhash, password)

	def __repr__(self):
		return '<User {0}>'.format(self.username)



	