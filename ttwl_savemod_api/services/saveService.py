import os

from ttwlsave.ttwlsave import TTWLSave
from ttwl_savemod_api.models.set_item_level_request import SetItemLevelRequest

class SaveService():
    def __init__(self, base_save_path: str) -> None:
        self.base_path = base_save_path
    
    def set_item_levels(self, request: SetItemLevelRequest) -> None:
        save = TTWLSave(os.path.join(self.base_path, request.filename))
        
        if request.level:
            to_level = request.level
        else:
            to_level = save.get_level()
        
        items = save.get_items()
        
        for item in items:
            if item.level != to_level:
                item.level = to_level

        save.save_to(os.path.join(self.base_path, request.out_filename))
