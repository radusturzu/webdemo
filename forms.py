from wtforms import Form, BooleanField, TextField, DateField, TextAreaField, PasswordField, validators, SelectField
from datetime import datetime, timedelta
#from wtforms_components import 
from wtforms.fields.html5 import DateField

class Forms1(Form):
	firstname = TextField('First name',  [validators.Length(min=4, max=25)], default='John')
	lastname = TextField('Last name',  [validators.Length(min=4, max=25)], default='Doe')
	email = TextField('Email Address', [
		validators.Length(min=6, max=35), validators.Regexp(message='Not a proper email, sorry.', regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$')
		], id="email", default='johndoe@yahoo.com')
	password = PasswordField('New Password', [
		validators.Required(),
		validators.EqualTo('confirm', message='Passwords must match')
	])
	confirm = PasswordField('Repeat Password')
	country = SelectField(u'Country of residence', id="country",choices=[('canada', 'Canada'), ('usa', 'USA'), ('europe', 'Europe'),('asia', 'Asia')])
	location = TextField('Location', [validators.Length(min=4, max=25)], default='City')
	birthdate = DateField(u'Date of birth', 
		[validators.Required()], 
		format='%Y-%m-%d', id="datepicker")
	accept_tos = BooleanField('I accept the TOS', [validators.Required()], id="required")
