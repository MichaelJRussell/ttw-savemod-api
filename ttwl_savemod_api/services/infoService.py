import os
from ..models.character_info import CharacterInfo
from ttwlsave.ttwlsave import TTWLSave

class InfoService:
    def __init__(self, base_save_path: str) -> None:
        self.base_path = base_save_path
    
    def get_info(self, filename: str, extended: bool = False):
        save = TTWLSave(os.path.join(self.base_path, filename))
        info = CharacterInfo()
        
        info.name = save.get_char_name()
        info.saveId = save.get_savegame_id()
        info.level = save.get_level()

        return info
