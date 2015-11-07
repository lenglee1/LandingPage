from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):
	__tablename__ = 'users'
	uid = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(64), unique = True, index = True)
	food_choice = db.Column(db.String(64))
	employment_status = db.Column(db.String(64)) 

	def __repr__(self):
		return '<User {0}>'.format(self.username)





	