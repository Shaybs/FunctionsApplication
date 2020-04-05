from flask import abort, render_template, redirect, url_for, request, flash
from application import app, bcrypt
import requests

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
	value_json = requests.post('https://shaybsapp.azurewebsites.net/api/centralserver?code=qgixZAslpaGvBpqTnMOp2cVBvct6UozfMCQRwuNHIKZhGXTY2utsag==')
    value = value_json.json()["Value"]
	return render_template('value.html', title='Functions Application', value=value)



