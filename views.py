#to start db call this in shell
#>>> from flaskr import init_db
#>>> init_db()

#to aoid circular dependencies, use import style only

# all the imports

import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
	render_template, flash, jsonify

from app import app
from database import get_db, connect_db
from forms import Forms1

@app.route('/ajax')
def ajax():
    return render_template('ajax.html')

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)



	
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	userFound = False
	passwordCorrect = False
	
	#calling db
	db = get_db()
	cur = db.execute('select username, password from users order by usid desc')
	entries = cur.fetchall()
	
	
	if request.method == 'POST':
		#gets user info
		for entry in entries:
			if request.form['username'] == entry[0]:
				userFound = True
				if request.form['password'] == entry[1]:
					passwordCorrect = True
		
		#performs check on user info
		if not userFound:
			error = 'Invalid username'
		elif not passwordCorrect:
			error = 'Invalid password'
		else:
			session['logged_in'] = True
			session['currentuser'] = request.form['username']
			cur2 = db.execute('select usid from users where username=?',(session['currentuser'],))
			session['currentuserid']= cur2.fetchone()['usid']
	
			flash('You were logged in')
			return redirect(url_for('show_entries'))
	return render_template('login.html', error=error)
	

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('show_entries'))

@app.route('/', methods=['GET', 'POST'])
@app.route('/forms1', methods=['GET', 'POST'])
def forms1():
	form = Forms1(request.form)
	if request.method == 'POST' and form.validate():
		#db = get_db()
		#db.execute('insert into users (username,email,password, birthdate, location, postcount) values (?, ?, ?, ?, ?, ?)',
		#	[form.username.data, form.email.data, form.password.data, form.birthdate.data, form.location.data, 0])
		#db.commit()
		flash('Thanks for posting form info')
		return redirect(url_for('login'))
	return render_template('forms1.html', form=form)
