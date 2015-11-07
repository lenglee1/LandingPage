from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField, RadioField
from wtforms.validators import Required


class DataForm(Form):
	name = StringField("What's your name, love?")
	food_choice = SelectField("Preferred sustenance: ", choices=[(1, "Fruit"), (2, "Vegetables"), (3, "Meat")], default=2)
	employment_status = RadioField('Label?', choices = [(1, 'Unemployed'), (2, 'Student'), (3, 'Employed')])
	submit = SubmitField('Submit')


	

