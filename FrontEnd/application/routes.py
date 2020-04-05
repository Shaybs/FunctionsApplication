from flask import abort, render_template, redirect, url_for, request, flash
from application.forms import RegistrationForm, LoginForm, UpdateAccountForm, CountryForm
from application.models import Users
from application import app, db, bcrypt, login_manager
import requests
from flask_login import login_user, current_user, logout_user, login_required

#Render the home page
@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')

#Render the about page
@app.route('/about')
def about():
	return render_template('about.html', title='About')

#Render the about page
@app.route('/value', methods=['GET', 'POST'])
def value():

	
	value = requests.post('https://shaybsapp.azurewebsites.net/api/centralserver?code=qgixZAslpaGvBpqTnMOp2cVBvct6UozfMCQRwuNHIKZhGXTY2utsag==')
	if value.ok:
		flash('New Value!')
		return redirect(url_for('value'))

	return render_template('value.html', title='Functions Application', user=user)



