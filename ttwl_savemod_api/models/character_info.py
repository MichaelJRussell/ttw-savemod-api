from marshmallow import Schema, fields

class CharacterInfo:
    def __init__(self) -> None:
        self.name = ''
        self.level = 0
        self.saveId = 0
    
    def __repr__(self):
        return '<CharacterInfo(name={self.name!r})>'.format(self=self)

class CharacterInfoSchema(Schema):
    name = fields.Str()
    level = fields.Number()
    saveId = fields.Number()
