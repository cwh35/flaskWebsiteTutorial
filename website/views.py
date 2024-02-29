# Used to store the URL endpoints for the frontend part of the website
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
# route for the home page
def home():
    return render_template("home.html")

