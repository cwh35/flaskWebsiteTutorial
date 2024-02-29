# Set up flask application
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'this key is not so secret'

    from .views import views
    from .auth import auth

    # only a slash '/' means no prefix to go to the route
    # registering blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app