"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, jsonify
from bs4 import BeautifulSoup
import requests, os, time, random
import urlparse
from flask_wtf import Form
from app.models import Profile
from forms import RegisterForm
from random import randint




###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')
    
@app.route('/api/users/register', methods=['POST'])
def register():
    # json_data = json.loads(request.data)
    form = RegisterForm()
    
    if request.method == 'POST':
        userid = random.randint(2500, 30000)
        username = request.form['username']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        age = request.form['age']
        sex = request.form['sex']
        image = request.files['image']
        profile_added_on = time.strftime("%d %B %Y")
        
        profile = Profile(username, userid, firstname, lastname, image, sex, age, profile_added_on)
        db.session.add(profile)
        db.session.commit()
        print ("NEW USER ADDED")
        


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to tell the browser not to cache the rendered page.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
