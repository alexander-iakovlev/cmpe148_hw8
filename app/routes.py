from app import myapp_obj
#from app.models import User
#from app.models import Post
#from app import db


from flask import render_template, flash, redirect, url_for, request
from datetime import datetime
#----------------------------------------------------------------------------#

@myapp_obj.route("/")
def home():
    return render_template('home.html', title='CMPE 148 HW 8')
