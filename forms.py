#forms.py

from flask_wtf import Form
from wtforms import StringField, DateField, IntegerField, \
SelectField, PasswordField, FileField
from wtforms.validators import DataRequired, Length, EqualTo

class AddPropertyForm(Form):
	property_ID = IntegerField()
	photo = FileField()
	title = StringField('Property Title', validators = [DataRequired()])
	posted_date = DateField('Current Date (mm/dd/yyyy)',
		validators=[DataRequired()], format='%m/%d/%Y'
		)
	sell_type = SelectField(
		'sell_type',
		validators=[DataRequired()],
		choices=[
		('fixed', 'fixed'), ('bid', 'bid')
		]
		)
	amount= IntegerField('amount')
	zipcode = IntegerField('zipcode')
	description = StringField('Description', validators=[DataRequired()])
	Num_Of_Bedrooms = IntegerField('Number of Bedrooms')
	size = StringField('Home Size (10M by 15M')
	location = StringField('Location', validators=[DataRequired()])
	status = IntegerField()

class Registration(Form):
	id = IntegerField()
	name = StringField('Full Names', validators = [DataRequired()])
	username = StringField('User Name', validators = [DataRequired()])
	user_type = SelectField('Type of User', validators = [DataRequired()], \
		choices=[('Owner', 'Agent', 'Buyer'), ('Owner', 'Agent', 'Buyer')]
		)
	SSNO = IntegerField()
	city = StringField('City of Residence')
	address = StringField('Home Address', validators= [DataRequired()])
	zipcode = IntegerField('Zipcode', validators = [DataRequired()])
	email = StringField('Email', validators=[DataRequired()])
	date = DateField('Current Date (mm/dd/yyyy)',
		validators=[DataRequired()], format='%m/%d/%Y'
		)
	cellphone = StringField()
	telephone = StringField('Tellphone Number')
	password = PasswordField('password', validators=[DataRequired(), Length(min=6, max=40)])
	confirm = PasswordField('Repeat password', validators=[DataRequired(), \
		EqualTo('password', message='Password must match')])
		

class Login(Form):
	username = StringField('User Name', validators = [DataRequired()])
	password = PasswordField('password', validators = [DataRequired()])

class GenerateBought(Form):
	date_bought = DateField('Current date (mm/dd/yyyy)', validators=[DataRequired()], format='%m%d%Y')
	owner_remarks = StringField()
	agent_remarks = StringField()
	buyer_remarks = StringField()

class CreateZipcode(Form):
	zipcode_ID = IntegerField()
	zipcode = IntegerField('Zipcode', validators= [DataRequired()])
	agent = StringField()
class Post(Form):
	title = StringField('title', validators=[DataRequired()])
	post = StringField('post', validators=[DataRequired()])
