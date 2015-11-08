from flask import Flask, render_template, request, redirect, url_for
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from forms import DataForm, LoginForm
from models import db, Pref, User



app = Flask(__name__)
bootstrap = Bootstrap(app)
manager = Manager(app)
db.init_app(app)

app.config['SECRET_KEY'] = "string"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:dog@localhost/development'


@app.route('/', methods = ['GET', 'POST'])
def index():
	login_form = LoginForm()

	if request.method == 'POST':
		newuser = User(email = login_form.email.data, username = login_form.username.data, password = login_form.pwdhash.data)
		db.session.add(newuser)
		db.session.commit()

		return redirect(url_for('survey')) 

	elif request.method == 'GET':
		return render_template('index.html', form = login_form)



@app.route('/survey', methods=['GET', 'POST'])
def survey():
	data_form = DataForm()

	if request.method == 'POST':
		newpref = Pref(bio = data_form.bio.data, food_choice = data_form.food_choice.data, employment_status = data_form.employment_status.data)
		db.session.add(newpref)
		db.session.commit()

		return render_template('success.html')

	elif request.method == 'GET':
		return render_template('survey.html', form = data_form)


@app.route('/testdb')
def testdb():
	if db.session.query("1").from_statement("SELECT 1").all():
		return "it works. i dont believe it!"
	else:
		return "shit not working. fuck fuck fuck."



if __name__ == '__main__':
	# manager.run()
	app.run(debug =True)


























