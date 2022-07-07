import os

from pprint import pprint
from ttwl_savemod_api.models.character_info_ext import CharacterInfoExt
from ..models.character_info import CharacterInfo
from ttwlsave.ttwlsave import TTWLSave

class InfoService:
    def __init__(self, base_save_path: str) -> None:
        self.base_path = base_save_path
    
    def get_info(self, filename: str, extended: bool = False):
        save = TTWLSave(os.path.join(self.base_path, filename))
        
        if not extended:
            info = CharacterInfo()
            
            info.name = save.get_char_name()
            info.saveId = save.get_savegame_id()
            info.level = save.get_level()
        else:
            info = CharacterInfoExt()
            items = {}
            equipped = []
            items['equipped'] = equipped
            
            info.name = save.get_char_name()
            info.saveId = save.get_savegame_id()
            info.level = save.get_level()
            info.items = items
            
            raw_items = save.get_equipped_items(True)
            
            if any(raw_items.values()):
                for (slot, item) in raw_items.items():
                    if item:
                        try:
                            if item.eng_name:
                                equipped.append('{}: {} ({}) ({}): {}'.format(slot, item.eng_name, item.level, item.item_type, item.get_serial_base64()))
                            else:
                                equipped.append('{}: unknown item: {}'.format(slot, item.get_serial_base64()))
                        except:
                            pprint(vars(item))
                            print("Could not parse {}".format(item.get_serial_base64()))

        return info
