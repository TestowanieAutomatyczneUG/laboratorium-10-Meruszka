class Note:
    def __init__(self, nazwa, nota) -> None:
        self.name = self._valid_name(nazwa)
        self.note = self._valid_note(nota)
    
    def _valid_name(self, name):
        if isinstance(name, str):
            if name is not None:
                return name
        raise ValueError
    
    def _valid_note(self, note):
        if isinstance(note, (float, int)):
            if note >= 2 and note <= 6:
                return note
            raise ValueError
        raise ValueError
    
    def get_name(self):
        return self.name
    
    def get_note(self):
        return self.note
