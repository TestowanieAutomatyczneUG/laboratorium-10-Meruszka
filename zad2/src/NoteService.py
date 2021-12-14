from zad2.src.NoteStorage import NotesStorage


class NotesSerivce:
    def __init__(self):
        self.notes = NotesStorage()

    def add(self, note):
        return self.notes.add(note)
    
    def averageOf(self, name):
        x = self.notes.getAllNotesOf(name)
        suma = 0
        for i in x:
            suma += i.note
        if len(x) != 0:
            return round(suma/len(x), 2)
        return 0
    
    def clear(self):
        return self.notes.clear()