# Used to store the URL endpoints for the frontend part of the website
from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
# route for the home page
def home():
    return render_template("home.html")

