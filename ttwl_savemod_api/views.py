from flask import Blueprint
from ttwl_savemod_api import app

hello = Blueprint('hello', __name__)

@app.route('/hello')
def index():
    return 'Hello World!'
