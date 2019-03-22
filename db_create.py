#flask/db_create.py

from views import db
from models import Property, User
from datetime import date


#create the database and the db table
try:
	db.create_all()
	print('Tables were created successfully')
except Exception as e:
	print('Error while creating tables')
	print(e)


#insert data

#commit the changes
db.session.commit()



