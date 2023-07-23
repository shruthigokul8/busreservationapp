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
app.config["SECRET_KEY"] = "ENTER YOUR SECRET KEY"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.init_app(app)

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True,
                         nullable=False)
    password = db.Column(db.String(250),
                         nullable=False)
    
db.init_app(app)
with app.app_context():
    db.create_all()
    
@login_manager.user_loader
def loader_user(user_id):
    return Users.query.get(user_id)

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

@app.route('/signup', methods=["GET", "POST"])
def signup():
  # If the user made a POST request, create a new user
    if request.method == "POST":
        user = Users(username=request.form.get("username"),
                     password=request.form.get("password"))
        # Add the user to the database
        db.session.add(user)
        # Commit the changes made
        db.session.commit()
        # Once user account created, redirect them
        # to login route (created later on)
        return redirect(url_for("login"))
    # Renders sign_up template if user made a GET request
    return render_template("signup.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    # If a post request was made, find the user by
    # filtering for the username
    if request.method == "POST":
        user = Users.query.filter_by(
            username=request.form.get("username")).first()
        # Check if the password entered is the
        # same as the user's password
        if user.password == request.form.get("password"):
            # Use the login_user method to log in the user
            login_user(user)
            return redirect(url_for("home"))
        # Redirect the user back to the home
        # (we'll create the home route in a moment)
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
    