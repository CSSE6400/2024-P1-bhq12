from flask import Flask
from .views.routes import api

def create_app():
    print('Create_app')
    app = Flask(__name__)    
    print('Flasked')
    app.register_blueprint(api)
    print('registered blueprint')

    return app
