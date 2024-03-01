from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

# defining login, logout, and sign up routes & URLs
@auth.route('/login')
def login():
    # you can pass variables to your templates that show up on the website
    # example, text="testing" will show up on the login page
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")