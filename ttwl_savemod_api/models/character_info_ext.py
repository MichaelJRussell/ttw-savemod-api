from marshmallow import Schema, fields
from ttwl_savemod_api.models.character_info import CharacterInfo, CharacterInfoSchema
from ttwl_savemod_api.models.item import ItemSchema

class CharacterInfoExt(CharacterInfo):
    def __init__(self) -> None:
        self.items = Items()
    
    def __repr__(self):
        return '<CharacterInfoExt(name={self.name!r})>'.format(self=self)

class Items:
    def __init__(self) -> None:
        self.equipped = []
        self.inventory = []

class ItemSchema2(Schema):
    equipped = fields.List(fields.Nested(ItemSchema))
    inventory = fields.List(fields.Nested(ItemSchema))

class CharacterInfoExtSchema(CharacterInfoSchema):
    items = fields.Nested(ItemSchema2)
