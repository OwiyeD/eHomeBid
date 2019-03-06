#flask/db_create.py

import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:

	#get a cursor object used to execute SQL
	c = connection.cursor()

	#create the table
	c.execute("""CREATE TABLE agents (
		agent_ID INTEGER PRIMARY KEY AUTOINCREMENT,
		ID INT NOT NULL, 
		name TEXT NOT NULL, 
		Num_Of_Zipcodes INT)"""
		)
	c.execute('INSERT INTO agents(ID, name, Num_Of_Zipcodes)'
		'Values(29434176, "Douglas Owiye", 0)')