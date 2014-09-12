#to start db call this in shell
#>>> from flaskr import init_db
#>>> init_db()

# all the imports

import os
from contextlib import closing
from flask import Flask
from flask.ext.login import LoginManager

#application

app = Flask(__name__)
app.config.from_object(__name__)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

# Load default config and override config from an environment variable
app.config.update(dict(
	DATABASE=os.path.join(app.root_path, 'flaskr.db'),
	DEBUG=True, #never in production, as client oculd execute code
	SECRET_KEY='development key', #for safety
	CSRF_ENABLED = True,
	USERNAME='admin',
	PASSWORD='default'
))

#it is a good idea to load a separate, environment specific configuration file
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

login_manager = LoginManager()