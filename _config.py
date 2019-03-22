import os

#get the file where this script is kept
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'houses.db'
CSRF_ENABLED =True
SECRET_KEY = 'myprecious'

#define the full path to the dabase
DATABASE_PATH = os.path.join(basedir, DATABASE)

#the database uri
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
'sqlite:///' + DATABASE_PATH
SQLALCHEMY_TRACK_MODIFICATIONS = True