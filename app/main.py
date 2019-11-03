# pip installed
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = MySQL(app)

from controllers.produto import *

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

