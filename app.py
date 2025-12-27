from flask import Flask

from profiles import profile


app = Flask(__name__)

app.register_blueprint(profile)