from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 

UPLOAD_FOLDER = './uploads/' 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///testdata.db'
app.config['SECRET_KEY'] ="f%U]pXCDWd}J85f["

db = SQLAlchemy(app)  

from app import home
from app import input_form
from app import add_id
from app import update_id
from app import delete_id 
from app import accounts 
from app import category
from app import dates
from app import chart
from app import calendar 
from app import download 
from app import upload
