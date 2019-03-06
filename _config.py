import os

#get the file where this script is kept
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'houses.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED =True
SECRET_KEY = 'myprecious'

#define the full path to the dabase
DATABASE_PATH = os.path.join(basedir, DATABASE)