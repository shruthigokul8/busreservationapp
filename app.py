import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from sqlalchemy.sql import text

db = SQLAlchemy()
# create the app
app = Flask(__name__)
# change string to the name of your database; add path if necessary
db_name = 'busticketreservations.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# initialize the app with Flask-SQLAlchemy
db.init_app(app)


# NOTHING BELOW THIS LINE NEEDS TO CHANGE
# this route will test the database connection - and nothing more
@app.route('/')
def home():
    return render_template('main.html')


@app.route('/customer/')
def customer():
    return render_template('customer.html')


@app.route('/admin/')
def administrator():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)