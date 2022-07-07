from marshmallow import Schema, fields
from ttwl_savemod_api.models.character_info import CharacterInfo, CharacterInfoSchema

class CharacterInfoExt(CharacterInfo):
    def __init__(self) -> None:
        self.items = Items()
    
    def __repr__(self):
        return '<CharacterInfoExt(name={self.name!r})>'.format(self=self)

class Items:
    def __init__(self) -> None:
        self.equipped = []
        self.inventory = []

class ItemSchema(Schema):
    equipped = fields.List(fields.Str())
    inventory = fields.List(fields.Str())

class CharacterInfoExtSchema(CharacterInfoSchema):
    items = fields.Nested(ItemSchema)
