from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = "$up3rkey"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:project1@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 

db = SQLAlchemy(app)




from app import views

