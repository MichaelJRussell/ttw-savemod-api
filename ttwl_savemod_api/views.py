from flask import Blueprint
from flask import jsonify, request
from ttwl_savemod_api import app
from ttwl_savemod_api.models.character_info import CharacterInfoSchema
from ttwl_savemod_api.models.character_info_ext import CharacterInfoExtSchema
from ttwl_savemod_api.models.set_item_level_request import SetItemLevelRequest
from ttwl_savemod_api.services.infoService import InfoService
from ttwl_savemod_api.services.saveService import SaveService

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

@app.route('/saves/<filename>/level_items', methods=['POST'])
def set_item_levels(filename: str):
    request_vars = SetItemLevelRequest(filename, request.json)
    service = SaveService(app.config['SAVE_DIR'])
    
    service.set_item_levels(request_vars)

    return "", 204
