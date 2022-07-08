import os

from pprint import pprint
import typing
from ttwl_savemod_api.models.character_info_ext import CharacterInfoExt
from ttwl_savemod_api.models.item import Item
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
            
            info.name = save.get_char_name()
            info.saveId = save.get_savegame_id()
            info.level = save.get_level()
            info.items = items
            
            raw_items = save.get_equipped_items(True)
            items['equipped'] = self.build_item_list(raw_items)
            
            raw_items = save.get_items()
            inv_items = []
            
            print(f'Num inv items: {len(raw_items)}')
            
            if len(raw_items) > 0:
                for item in raw_items:
                    print(f' - {item.eng_name}')
                    try:
                        newItem = Item('', item.get_serial_base64())
                        if item.eng_name:
                            newItem.name = item.eng_name
                            newItem.level = item.level
                            newItem.type = item.item_type
                    except:
                        newItem = None
                        print(f"Parse error ")
                        pprint(item)
                
                    if newItem:
                        inv_items.append(newItem)

            items['inventory'] = inv_items
            
        return info

    def build_item_list(self, raw_items) -> typing.List[Item]:
        item_list = []
        
        if any(raw_items.values()):
            for (slot, item) in raw_items.items():
                if item:
                    try:
                        newItem = Item(slot, item.get_serial_base64())
                        item_list.append(newItem)
                        
                        if item.eng_name:
                            newItem.name = item.eng_name
                            newItem.level = item.level
                            newItem.type = item.item_type
                    except:
                        pprint(vars(item))
                        print("Could not parse {}".format(item.get_serial_base64()))
        
        return item_list
