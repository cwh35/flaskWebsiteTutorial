# Used to store the URL endpoints for the frontend part of the website
from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
# route for the home page
def home():
    return "<h1>Test</h1>"

