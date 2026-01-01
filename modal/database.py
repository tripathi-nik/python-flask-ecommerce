from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
db = SQLAlchemy()
load_dotenv()

MYSQL_HOST = os.environ.get('MYSQL_HOST')
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_DB = os.environ.get('MYSQL_DB')
MYSQL_INSTANCE_CONNECTION=os.environ.get('MYSQL_INSTANCE_CONNECTION')