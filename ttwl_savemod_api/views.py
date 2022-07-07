import os
from flask import Blueprint
from flask import jsonify
from ttwl_savemod_api import app
from ttwl_savemod_api.models.character_info import CharacterInfoSchema
from ttwl_savemod_api.services.infoService import InfoService

hello = Blueprint('hello', __name__)
ttwl_info_bp = Blueprint('ttwl_info_bp', __name__)

@app.route('/hello')
def index():
    return 'Hello World!'

@app.route('/info/<filename>', methods=['GET'])
def get_info(filename: str):
    service = InfoService(app.config['SAVE_DIR'])
    raw_info = service.get_info(filename)
    schema = CharacterInfoSchema()
    info = schema.dump(raw_info)

    return jsonify(info)
