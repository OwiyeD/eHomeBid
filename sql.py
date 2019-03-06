import sqlite3

conn = sqlite3.connect('new.db')

cursor = conn.cursor()

cursor.execute("""CREATE TABLE if not exists agent(
	agent_ID INT PRIMARY KEY NOT NULL, 
	agent_Name TEXT NOT NULL, 
	purchased_Zipcodes INT NOT NULL
	);
	""")
cursor.execute("""CREATE TABLE if not exists buyer(
	buyer_ID INT PRIMARY KEY NOT NULL, 
	buyer_Name TEXT NOT NULL, 
	location TEXT NOT NULL
	);
	""")
cursor.execute("""CREATE TABLE if not exists owner(owner_ID INT PRIMARY KEY NOT NULL, 
	owner_Name TEXT NOT NULL, 
	location TEXT NOT NULL
	);
	""")
cursor.execute("""CREATE TABLE if not exists zipcode(zipcode INT PRIMARY KEY NOT NULL,
status NOT NULL,
date_created DATE,
price INT NOT NULL,
agent_ID INT,
location TEXT NOT NULL
)
""")
cursor.execute("""CREATE TABLE if not exists house(house_ID INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
location TEXT,
size TEXT,
zipcode INT NOT NULL,
number_Of_Rooms INT,
picture BLOB,
purchase_Type TEXT
)
""")
conn.close