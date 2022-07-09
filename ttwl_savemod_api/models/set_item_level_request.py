class SetItemLevelRequest:
    def __init__(self, filename: str, json: dict[str, str]) -> None:
        self.filename = filename
        self.out_filename = json['outFilename']
        self.level = int(json['level'])
