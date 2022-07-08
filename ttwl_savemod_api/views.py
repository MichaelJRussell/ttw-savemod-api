from flask import Blueprint
from flask import jsonify, request
from ttwl_savemod_api import app
from ttwl_savemod_api.models.character_info import CharacterInfoSchema
from ttwl_savemod_api.models.character_info_ext import CharacterInfoExtSchema
from ttwl_savemod_api.services.infoService import InfoService

hello = Blueprint('hello', __name__)
ttwl_save_bp = Blueprint('ttwl_save_bp', __name__)

@app.route('/hello')
def index():
    return 'Hello World!'

@app.route('/saves/<filename>', methods=['GET'])
def get_info(filename: str):
    is_extended = request.args.get('extended')
    service = InfoService(app.config['SAVE_DIR'])
    raw_info = service.get_info(filename, is_extended)
    
    if is_extended:
        schema = CharacterInfoExtSchema()
    else:
        schema = CharacterInfoSchema()
        
    info = schema.dump(raw_info)

    return jsonify(info)
