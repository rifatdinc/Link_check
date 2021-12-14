
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://radius:radpass@localhost:5432/Link'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)




class nas(db.Model):
    __tablename__ = 'nas'
    nasid = db.Column(db.Integer, primary_key=True,
                   unique=True, autoincrement=True)
    nasname = db.Column(db.String, nullable=False)
    nassip = db.Column(db.String, nullable=False)
    nasuser = db.Column(db.String, nullable=False)
    nasspasswd = db.Column(db.String, nullable=False)



class macaddrs(db.Model):
    id = db.Column(db.Integer, primary_key=True,
                unique=True, autoincrement=True)
    mac = db.Column(db.String,nullable=False)
    company_name = db.Column(db.String,nullable=False)

    def __init__(self,mac,company_name):
        self.mac =mac 
        self.company_name =company_name
        
db.create_all()
db.session.remove()