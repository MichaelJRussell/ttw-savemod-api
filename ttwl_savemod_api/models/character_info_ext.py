from ttwl_savemod_api.models.character_info import CharacterInfo

class CharacterInfoExt(CharacterInfo):
    def __init__(self) -> None:
        self.items = {}
    
    def __repr__(self):
        return '<CharacterInfoExt(name={self.name!r})>'.format(self=self)
