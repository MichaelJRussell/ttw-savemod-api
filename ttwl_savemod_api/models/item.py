from marshmallow import Schema, fields

class Item:
    def __init__(self, slot:str = '', serial_base_64:str = '') -> None:
        self.name = ''
        self.level = 0
        self.type = ''
        self.slot = slot
        self.serial_base_64 = serial_base_64
        
    def __repr__(self):
        return '<Item(name={self.serial_base_64!r})>'.format(self=self)

class ItemSchema(Schema):
    name = fields.Str()
    level = fields.Number()
    type = fields.Str()
    slot = fields.Str()
    serial_base_64 = fields.Str()
