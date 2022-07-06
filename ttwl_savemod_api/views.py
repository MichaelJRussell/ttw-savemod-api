import imp
import json
from flask import Blueprint
from flask import jsonify
from ttwl_savemod_api import app
from ttwlsave.ttwlsave import TTWLSave

hello = Blueprint('hello', __name__)
ttwl_info_bp = Blueprint('ttwl_info_bp', __name__)

@app.route('/hello')
def index():
    return 'Hello World!'

@app.route('/info/<filename>', methods=['GET'])
def get_info(filename: str):
    save = TTWLSave(filename)
    info = {
        'name': save.get_char_name(),
        'saveId': save.get_savegame_id(),
        'level': save.get_level()
    }

    return jsonify(info)