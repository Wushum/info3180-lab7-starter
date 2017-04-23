"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, jsonify, flash
from flask_login import login_user, logout_user, current_user, login_required
from bs4 import BeautifulSoup
import requests, os, time, random
import urlparse
from flask_wtf import Form
from app.models import Profile, Wishlist
from forms import RegisterForm, LoginForm, WishForm
from random import randint
from image_getter import getImg

###
# Routing for your application.
###

#Landing
@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')
    
@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Project 2")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'danger')
    return redirect(url_for('login'))
    
### 
#API Routes

#Creates user, saves to database
@app.route("/api/users/register", methods=["POST"])
def register():
    form = RegisterForm()
    
    if request.method == 'POST':
        userid = random.randint(2500, 30000)
        username = request.form['username']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        gender = request.form['gender']
        password  = request.files['password']
        profile_added_on = time.strftime("%d %B %Y")
        
        profile = Profile(userid=userid, username=username, firstname=firstname, lastname=lastname, email=email, gender=gender, password=password, profile_added_on=profile_added_on)
        db.session.add(profile)
        db.session.commit()
        flash('Profile for '+ username +' added','success')    
        return redirect(url_for('home'))
    return render_template('register.html', form = form)

#login 
@app.route("/api/users/login", methods=["POST"])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        
        #if form.username.data:
            username = form.username.data
            password = form.password.data
            user = Profile.query.filter_by(username=username, password=password).first()
            if user is not None:
            
                login_user(user)
                flash('Logged in Successfully.', 'success')
                next = request.args.get('next')
            
                return redirect(url_for('home'))
            else:
                flash('Username or Password is incorrect.', 'danger')
                return redirect(url_for('login'))
    return render_template("login.html", form=form)

#Adding items to wishlist #Returns a user's wishlist
@app.route("/api/users/{userid}/wishlist", methods=["GET","POST"])
def wishlist(userid):
    if request.method == "GET":
        wishes = Wishlist.query.filter_by(userid=current_user.get_id()).all()

    elif request.method == "POST":
        form = WishForm()
        if form.validate_on_submit():
            userid = current_user.get_id()
            title = form.title.data
            description = form.description.data
            url = form.url.data
            thumbnail = form.thumbnail.data
            created_on = #gettime
            itemid = random.randint(2500, 30000)

            newitem = WishList(
                            itemid=itemid,
                            userid=userid,
                            title=title,
                            description=description,
                            url=url,
                            thumbnail=thumbnail,
                            created_on = created_on)

            db.session.add(newitem)
            db.session.commit()
    return render_template("wishlist.html", userid=current_user.get_id(), form=form, wishes=wishes)

#Accepts URL, returns JSON list of thumbnails
@app.route("/api/thumbnails", methods=["GET"])
def thumbnails():
    url = request.args.get("url")
    if url == "":
        return jsonify({"error": "1","data": {},"message": "Unable to extract thumbnails"})
    else:
        thumbs = {'thumbails':getImg(url)}
        return jsonify(error='Null', thumbs=thumbs, message="Success")

#Deletes item from user's wishlist
@app.route("/api/users/{userid}/wishlist/{itemid}", methods=["GET", "DELETE"])
@login_required
def deleteitem(userid, itemid):
    db.session.delete(Wishlist.query.filter_by(userid=userid,id=itemid).first())
    db.session.commit()
    return redirect (url_for("wishlist", userid=current_user.get_id()))


#
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
