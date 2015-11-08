from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField, RadioField, TextAreaField, validators, PasswordField
from wtforms.validators import InputRequired, Email


class DataForm(Form):
	bio = TextAreaField("What's your story, homie?")
	food_choice = SelectField("Preferred sustenance: ", choices=[(1, "Fruit"), (2, "Vegetables"), (3, "Meat")], default=2)
	employment_status = RadioField('Label?', choices = [(1, 'Unemployed'), (2, 'Student'), (3, 'Employed')])
	submit = SubmitField('Submit')


class LoginForm(Form):
	email = StringField("Email", [InputRequired("Please enter your email address."), Email("Please enter a valid email address.")]) 
	username = StringField("Username", [InputRequired("Please enter your username.")])
	pwdhash = PasswordField("Password", [InputRequired("Please enter your username.")])
	submit = SubmitField('Sign up')

