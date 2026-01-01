from flask import Flask
# from products import product
# from orders import order
from profiles import profile
from modal.database import db,MYSQL_HOST,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DB,MYSQL_INSTANCE_CONNECTION
from flask_login import LoginManager
from datetime import timedelta
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_DB}?unix_socket=/cloudsql/{MYSQL_INSTANCE_CONNECTION}'
app.config['SECRET_KEY'] = os.environ.get("HASH_KEY")
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

app.register_blueprint(profile) 
