from flask import Flask
from Time_Traking_Project.views.main import main

def create_app():
    app = Flask(__name__)
    app.debug = 1

    app.register_blueprint(main)

    return app
