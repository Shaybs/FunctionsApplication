from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import requests
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
bcrypt = Bcrypt(app)

from application import routes
