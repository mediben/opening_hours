from flask import Flask

#from models import BaseModel

"""
Initiated the weather alert app and set the configuration needed
"""
def create_app():
    opening_hours_app = Flask(__name__)
    # opening_hours_app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
    # opening_hours_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    opening_hours_app.app_context().push()


    return opening_hours_app

