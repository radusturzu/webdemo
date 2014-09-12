from flask import g
import sqlite3
from app import app

#Flaskr is a database powered application
def connect_db():
	"""Connects to the specific database."""
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row #treat rows as tuples
	return rv

#1 transaction / time - > use app. context (app context, request context:
# g and request var)
#Problem: requires the sqlite3 command to be installed which is not the case on every system.
#Its a good idea to add a function that initializes the database for you to the application.

def init_db():
	#The with app.app_context() statement establishes the application context for us. In the body of the 
	#with statement the g object will be associated with app.

	with app.app_context():
		db = get_db()
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit() #necessary


def get_db():
	"""Opens a new database connection if there is none yet for the
	current application context.
	"""
	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db

#Functions marked with teardown_appcontext() are called every time the app context tears down.
@app.teardown_appcontext
def close_db(error):
	"""Closes the database again at the end of the request."""
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()


