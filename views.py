#flask/views.py

from functools import wraps
from flask import Flask, flash, redirect, \
render_template, request, session, url_for 
from datetime import datetime
from forms import AddPropertyForm, Registration, Login, GenerateBought, CreateZipcode, Post
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#config
app = Flask(__name__)
app.config.from_object('_config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Property, User, Bid, Bought, Zipcode

#HELPER FUNCTIONS
def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash('Login First Please')
			return redirect(url_for('login'))
	return wrap
	#Error function
def flash_errors(form):
	for field, errors in form.errors.items():
		for error in errors:
			flash(u"Error in the %s field - %s"%(
				getattr(form, field).label.text, error), 'error')
#Properties functions
def open_properties():
	return db.session.query(Property).filter_by(
		status='0').order_by(Property.posted_date.desc())

def closed_properties():
	return db.session.query(Property).filter_by(
		status='1').order_by(Property.posted_date.asc())
def expired_properties():
	return db.session.query(Property).filter_by(
		status='2').order_by(Property.posted_date.asc())

def users():
	return db.session.query(User).order_by(User).username.asc()	

# A function to declare a property expired 
def expired(property_ID, due_date):
	if(due_date > today):
		new_id = property_ID
		db.session.query(Property).filter_by(property_ID=new_id).update({"status":"2"})
		db.session.commit()


#ROUTE HANDLERS
@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('Thank you for visiting')
	return redirect(url_for('main'))

#Landing page
@app.route('/')
def main():
	return render_template('main.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	form = Login(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			user = User.query.filter_by(username=request.form['username']).first()
			user_type = User.query.filter_by(username=request.form['user_type']).first()
			if user is not None and user.password==request.form['password']:
				if user_type == ('agent'):
					session['logged_in'] =True
					flash('Welcome')
					return redirect(url_for('agent'))
				elif user_type==('owner'):
					session['logged_in'] = True
					flash('Welcome')
					return redirect(url_for('owner'))
				else:
					session['logged_in'] = True
					flash('Welcome')
					return redirect(url_for('buyer'))
			else:
				error = 'Invalid Credentials. Please Try Again'
				return render_template('login.html')
	return render_template('login.html', error=error)

@app.route('/owner')
#@login_required
def owner():
	return render_template('owner.html')

@app.route('/agent')
def agent():
	return render_template('agent.html')

@app.route('/buyer')
def buyer():
	return render_template('buyer.html')

@app.route('/properties/')
#@login_required
def properties():

	#let us finnd our properties with status sold, Not sold or expired if not sold within assigned time
	return redirect(url_for('owner', 
		form=AddPropertyForm(request.form),
		open_properties=open_properties(), 
		closed_properties=closed_properties(),
		expired_properties=expired_properties(),
		users=users()
		))


@app.route('/new_property/', methods=['GET', 'POST'])
#@login_required
def new_property():
	error=None
	form = AddPropertyForm(request.form)
	if request.method == 'POST':
		try:
			if form.validate_on_submit():
				new_property = Property(
					form.photo.data,
					form.title.data,
					form.due_date.data,
					form.posted_date.data,
					form.sell_type.data,
					form.amount.data,
					form.zipcode.data,
					form.description.data,
					form.Num_Of_bedrooms.data,
					form.size.data,
					form.location.data,
					'0'
					#session['user_ID']
					)
				db.session.add(new_property)
				db.session.commit()
				flash('New property added successfully')
				return redirect(url_for('new_property'))
		except Exception as e:
			flash('We couldnt record the info')
		
	return render_template('new_property.html', form=form, error=error, name=session.get('name'))
		

#after the owner has posted hi property he/she may need to edit
@app.route('/edit/<int:property_ID>/', methods=['GET', 'POST'])
def edit(property_ID):
	new_id = property_ID
	return render_template('edit.html')


#Owner may close a property sell
@app.route('/complete/<int:property_ID>/')
def complete(property_ID):
	new_id = property_ID
	db.session.query(Property).filter_by(property_ID=new_id).update({"status":"0"})
	db.session.commit()
	flash('Thank you for being a valuable customer')
	return redirect(url_for('owner'))
	

#Owner may remove a property completely
@app.route('/remove/<int:property_ID>/')
def remove_property(property_ID):
	new_id = property_ID
	db.session.query(Property).filter_by(property_ID=new_id).delete()
	db.session.commit()
	flash('You have successfully removed a property from the listing')
	return redirect(url_for('owner'))
	

@app.route('/expired/<int:property_ID>/')
def expired(property_ID, due_date):
	if(due_date > today):
		new_id = property_ID
		db.session.query(Property).filter_by(property_ID=new_id).update({"status":"2"})
		db.session.commit()
		return redirect(url_for('owner'))



@app.route('/register/', methods=['GET', 'POST'])
def register():
	error = None
	form = Registration(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			new_user = User(
				form.name.data,
				form.username.data,
				form.user_type.data,
				form.ssno.data,
				form.city.data,
				form.address.data,
				form.zipcode.data,
				form.email.data,
				form.date.data,
				form.cellphone.data,
				form.telphone.data,
				form.password.data
				)
			db.session.add(new_user)
			db.session.commit()
			flash('Registration successfully. Kindly login')
			return redirect(url_for('login'))
		else:
			flash('You messed Up your registration')
			return redirect(url_for('register', error=error))			
	return render_template('register.html', form=form, error=error)


@app.route('/signup')
def signup():
	return render_template('signup.html')


@app.route('/post/', methods=['GET','POST'])
def post():
	error= None
	if request.method=='POST':
		new_post = (
			form.title.data,
			form.post.data
			)
		db.session.add(new_post)
		db.session.commit()
		flash('Successfully posted')
		return redirect(url_for('main'))
	return render_template('login.htm', error=error)
