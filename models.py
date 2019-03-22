#flask/models.py

from views import db
from datetime import datetime

class Property(db.Model):
	__tablename__= "properties"
	id = db.Column(db.Integer, primary_key=True)
	owner_ID = db.Column(db.Integer, db.ForeignKey('users.id'))
	photo = db.Column(db.LargeBinary, nullable=True)
	title = db.Column(db.String(70), nullable=False)
	due_date = db.Column(db.Date, nullable=False)
	posted_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	sell_type = db.Column(db.String, nullable=False)
	amount = db.Column(db.Integer, nullable=False)
	zipcode = db.Column(db.Integer, nullable=False)
	description = db.Column(db.String, nullable=False)
	Num_Of_Bedrooms = db.Column(db.Integer, nullable=False)
	size = db.Column(db.String, nullable=False)
	location = db.Column(db.String, nullable=False)
	status = db.Column(db.Integer, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __init__(self, photo, due_date, posted_date, \
		sell_type, amount, zipcode, description, Num_Of_Bedrooms, size, location, status):
		self.photo = photo
		self.due_date = due_date
		self.posted_date = posted_date
		self.sell_type = sell_type
		self.amount = amount
		self.zipcode = zipcode
		self.description = description
		self.Num_Of_Bedrooms = Num_Of_Bedrooms
		self.size = size
		self. location = location
		self. status =status

	def __repr__():
		return '<title {0}>'.format(self.name)

class User(db.Model):
	__tablename__= 'users_1'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	username = db.Column(db.String, unique=True, nullable=False)
	user_type = db.Column(db.String, nullable=False)
	SSNO = db.Column(db.Integer, unique=True, nullable=False)
	city = db.Column(db.String, nullable=False)
	address = db.Column(db.String, nullable=False)
	zipcode = db.Column(db.String, nullable=False)
	email = db.Column(db.String, unique=True, nullable=False)
	date = db.Column(db.Date, nullable=False)
	cellphone = db.Column(db.String, nullable=True)
	telphone = db.Column(db.String, nullable=True)
	password = db.Column(db.String, nullable=False)
	#properties_1 = db.relationship('Property', backref='poster')
	#zipcodes = db.relationship('Zipcode', backref='posser')

	def __init__ (self, name, username, user_type, SSNO, city, \
		address, zipcode, email, date, cellphone, telphone, password):
	    self.name = name
	    self.username = username
	    self.user_type = user_type
	    self.SSNO = SSNO
	    self.city = city
	    self.address = address
	    self.zipcode = zipcode
	    self.email = email
	    self.date = date
	    self.cellphone = cellphone
	    self.telphone = telphone
	    self.password = password

	def __repr__():
		return 
		'<User {0}>'.format(self.username)

class Bid(db.Model):
	__tablename__ = 'bids'
	bid_ID = db.Column(db.Integer, primary_key=True)
	home_ID = db.Column(db.Integer, db.ForeignKey('properties_1.id'), nullable=False)
	buyer_ID = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
	agent_ID = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
	owner_ID = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

	def __init__(self, home_title, buyer_username, agent_username, owner_username):
		self.home_title = home_title
		self.buyer_username = buyer_username
		self.agent_username = agent_username
		self.owner_username = owner_username

	def __repr__():
		return
		'<Bid {0}>'.format(self.home_title)


class Bought(db.Model):
	__tablename__ = 'boughts'
	bought_ID = db.Column(db.Integer, primary_key=True)
	home_ID = db.Column(db.Integer, db.ForeignKey('properties_1.id'), nullable=False)
	sell_type = db.Column(db.String, nullable=False)
	buyer_name = db.Column(db.String, nullable=False)
	amount = db.Column(db.Integer, nullable=False)
	date_bought = db.Column(db.Date, nullable=False)
	buyer_remarks = db.Column(db.String, nullable=True)
	owner_remarks = db.Column(db.String, nullable=True)
	agent_remarks = db.Column(db.String, nullable=True)


	def __init__(self, home_ID, sell_type, buyer_name, amount, date_bought, buyer_remarks, owner_remarks, agent_remarks):
		self.home_ID = home_ID
		self.sell_type = sell_type
		self.buyer_name = buyer_name
		self.amount = amount
		self.date_bought = date_bought
		self.buyer_remarks = buyer_remarks
		self.owner_remarks = owner_remarks
		self.agent_remarks = agent_remarks

	def __repr__():
		return
		'<Bought {0}>'.format(self.home_ID)

class Zipcode(db.Model):
	__tablename__ = 'zipcodes'
	zipcode_ID = db.Column(db.Integer, primary_key=True)
	zipcode = db.Column(db.Integer, nullable=False)
	agent_ID = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)

	def __init__(self, zipcode, agent_ID):
		self.zipcode = zipcode
		self.agent_ID = agent_ID

	def __repr__():
		return
		'<Zipcode {0}>'.format(self.zipcode)
		