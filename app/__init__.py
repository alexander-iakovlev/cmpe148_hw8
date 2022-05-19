from flask import Flask
import os


# what is the directory of the project
basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj = Flask(__name__)

myapp_obj.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess',
    # where to store app.db (database file)
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
)

from app import routes #, models
