import sqlite3

#the database is called home.db
with sqlite3.connect("home.db") as connection:
	c = connection.cursor()
	c.execute("""CREATE TABLE if not exists posts
		(title TEXT, post TEXT)""")
	#insert dummy data
	c.execute('INSERT INTO posts VALUES("Good", "I am good")')