#flask/views.py

import sqlite3
from functools import wraps
from flsk import Flask, flash, redirect, \
render_template, request, session, url_for

#config
app = Flask(__name__)
app.config.from_object('_config')

#helper functions

def connect_db():
	return sqlite3.connect(app.config['DATABASE_PATH'])

def login_required(test):
	@wraps(test)
	def wrap(*args. **kwargs):
		if 'login_in' in session:
			return test(*args, **kwargs)
		else:
			flash('Login First Please')
			return redirect(url_for('login'))
	return wrap


#Route handlers
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
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid Credentials. Please Try Again'
			return render_template('login.html')

		else:
			session['logged_in'] = True
			flash('Welcome')
			return redirect(url_for('agents'))
	return render_template('login.html')
