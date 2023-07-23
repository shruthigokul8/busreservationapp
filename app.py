import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from sqlalchemy.sql import text
import torch

db = SQLAlchemy()
# create the app
app = Flask(__name__)
# change string to the name of your database; add path if necessary
db_name = 'busticketreservations.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# initialize the app with Flask-SQLAlchemy
db.init_app(app)

#functionality
@app.route('/')
def home():
    return render_template("dashboard.html")

@app.route('/about', methods=['GET'])
def about():
    return render_template("about.html")

@app.route('/contact', methods=['GET'])
def contact():
    return render_template("contact.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route('/customerdetails', methods=['GET'])
def customerdetails():
    return render_template("customerdetails.html")

@app.route('/faq', methods=['GET'])
def faq():
    return render_template("faq.html")

@app.route('/landing', methods=['GET'])
def landing():
    return render_template("landing.html")

@app.route('/seating', methods=['GET', 'POST'])
def seating():
    return render_template("seating.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
    