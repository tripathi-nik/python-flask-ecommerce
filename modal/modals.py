from .database import db
from datetime import datetime
import bcrypt
from datetime import datetime
from flask_login import  UserMixin


class Profile(UserMixin,db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    username=db.Column(db.String(200), nullable=False, unique=True)
    email=db.Column(db.String(200), nullable=False, unique=True)
    password=db.Column(db.String(200), nullable=False)
    age=db.Column(db.Integer, nullable=False)
    sex=db.Column(db.String(10), nullable=False)
    createdAt=db.Column(db.DateTime, default=datetime.now)

    addr = db.relationship("Addr", back_populates="profile")
    orders = db.relationship("Orders", back_populates="profile")

   
    #def check_password(self,password):
     #   bcrypt.checkpw(password.encode("utf-8"),self.password.encode('utf-8'))

class Addr(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    address=db.Column(db.String(200), nullable=False)
    city=db.Column(db.String(100), nullable=False)
    state=db.Column(db.String(100), nullable=False)
    pincode=db.Column(db.String(20), nullable=False)
    user_id=db.Column(db.ForeignKey('profile.id'))
   
    profile = db.relationship("Profile",back_populates="addr")    

class Products(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    product_name=db.Column(db.String(200), nullable=False)
    description=db.Column(db.TEXT, nullable=False)
    slug=db.Column(db.String(200), nullable=False, unique=True)
    qty=db.Column(db.Integer, nullable=False)
    price=db.Column(db.FLOAT, nullable=False)

    orders = db.relationship("Orders", back_populates="product")

class Orders(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    user_id=db.Column(db.ForeignKey('profile.id'))
    product_id=db.Column(db.ForeignKey('products.id'))
    qty=db.Column(db.Integer, nullable=False)
    addr=db.Column(db.Integer, nullable=False)
    order_date=db.Column(db.DateTime, default=datetime.now)

    profile = db.relationship("Profile",back_populates="orders")
    product = db.relationship("Products",back_populates="orders")
