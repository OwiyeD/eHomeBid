from flask import Flask, render_template, request, session, \
flash, redirect, url_for, g
#from flask.ext.bootstrap import Bootstrap
#bootstrap = Bootstrap(app)

from functools import wraps

import sqlite3

#configuration
DATABASE = 'home.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'hard_to_guess'

app = Flask(__name__)

#pulls in app configuration by looking for UPPERCASE
app.config.from_object(__name__)

#connect to database function
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash('You need to log in first')
			return redirect(url_for('login'))
	return wrap

@app.route('/')
def main():
	g.db = connect_db()
	cur = g.db.execute('select *from posts')
	posts = [dict(title=row[0], post=row[1]) for row in cur.fetchall()]
	g.db.close()

	return render_template('main.html', posts=posts)

#Login
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	status_code = 200
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid credentials please try again'
			status_code = 401
		else:
			session['logged_in'] = True
			return redirect(url_for('agent'))
	return render_template('login.html', error=error), status_code

#Agent controller
@app.route('/agent')
@login_required
def agent():
	return render_template('agent.html')

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You have logged out')
	return redirect(url_for('main'))

@app.route('/owner')
def owner():
	return render_template('owner.html')
	
@app.route('/add', methods=['GET','POST'])
def add():
	if request.form:
		title = request.form['title']
		post = request.form['post']
		if not title or not post:
			flash("All fields are required")
			return redirect(url_for('add'))
		else:
			g.db = connect_db()
			g.db.execute('insert into posts (title, post) values(?,?)',
				[request.form['title'], request.form['post']])
			g.db.commit()
			g.db.close()
			flash('Successfully added')
			return redirect(url_for('add'))
	return render_template('add.html')


@app.route('/user/<name>')
def user(name):
	return '<h1>Hello!, %s</h1>' % name

@app.route("/name/<f_name>")
def give(f_name):
	if f_name.lower()=="douglas":
		return "Hello, {}".format(f_name), 200
	else:
		return "Not Found"


if __name__ == '__main__':
	app.run(debug=True)