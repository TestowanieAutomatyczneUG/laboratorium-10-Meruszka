import unittest
from zad2.src.NoteService import NotesSerivce
from zad2.src.NoteStorage import NotesStorage
from zad1.src.Note import Note
from unittest.mock import patch


class TestNotesService(unittest.TestCase):

    def setUp(self):
        self.temp = NotesSerivce()

    @patch.object(NotesStorage, 'add')
    def test_NotesService_add(self, mock_method):
        mock_method.return_value = 'OK'
        note = Note('Ocena', 4)
        self.assertEqual('OK', self.temp.add(note))

    @patch.object(NotesStorage, 'add')
    def test_NotesService_add_2(self, mock_method):
        mock_method.return_value = "dodana"
        note = Note('Spr', 4)
        self.assertEqual('dodana', self.temp.add(note))

    @patch.object(NotesStorage, 'add')
    def test_NotesService_add_3(self, mock_method):
        mock_method.return_value = ['Pracka']
        note = Note('Pracka', 2)
        self.assertEqual(['Pracka'], self.temp.add(note))

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_NotesService_averageOf1(self, mock_method):
        mock_method.return_value = []
        self.assertEqual(0, self.temp.averageOf('Kuba'))

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_NotesService_averageOf2(self, mock_method):
        mock_method.return_value = [Note('Spr', 4),
                                    Note('Praca Domowa', 3),
                                    Note('Kartkówka', 2),
                                    Note('Spr', 5),
                                    Note('Spr', 6)]
        self.assertEqual(4.0, self.temp.averageOf('Jan'))

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_NotesService_averageOf3(self, mock_method):
        mock_method.return_value = [Note('Spr', 2),
                                    Note('Praca Domowa', 4),
                                    Note('Kartkówka', 5),
                                    Note('Spr', 6),
                                    Note('Spr', 2)]
        self.assertEqual(3.8, self.temp.averageOf('Szymon'))

    @patch.object(NotesStorage, 'clear')
    def test_NotesService_clear(self, mock_method):
        mock_method.return_value = []
        self.assertEqual([], self.temp.clear())

    @patch.object(NotesStorage, 'clear')
    def test_NotesService_clear2(self, mock_method):
        mock_method.return_value = None
        self.assertEqual(None, self.temp.clear())

