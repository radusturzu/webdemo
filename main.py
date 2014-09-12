import os
from app import app
from database import *
from views import *
from forms import *

if __name__ == '__main__':
	if not os.path.isfile("flaskr.db"):
		init_db()
	app.run()
	