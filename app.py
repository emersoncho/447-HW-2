from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////C:\\Users\\emers\\Documents\\CMSC 447\\HW_2\\users.db'
db = SQLAlchemy(app)

class users(db.Model):
        id = db.Column(db.Integer, primary_key=True),
        name  = db.Column(db.String(20))
        points = db.Column(Integer)