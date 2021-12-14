from typing import NewType
from unittest import TestCase
from src.Note import Note

class TestNote(TestCase):
    def test_name_abc_3(self):
        n = Note('abc', 3)
        self.assertEqual(n.get_name(), 'abc')

    def test_name_zzzzzzzzzzzzzzz_4(self):
        n = Note('zzzzzzzzzzzzzzz', 4)
        self.assertEqual(n.get_name(), 'zzzzzzzzzzzzzzz')
    
    def test_name_abc_5_5(self):
        n = Note('abc', 5.5)
        self.assertEqual(n.get_note(), 5.5)
    
    def test_name_abc_3_3(self):
        n = Note('abc', 3.3)
        self.assertEqual(n.get_note(), 3.3)
    
    def test_name_none_3(self):
        self.assertRaises(ValueError, Note, None, 3)
    
    def test_name_abc_1(self):
        self.assertRaises(ValueError, Note, 'abc', 1)
    
    def test_name_not_str(self):
        self.assertRaises(ValueError, Note, {}, 2)
    
    def test_name_not_str2(self):
        self.assertRaises(ValueError, Note, [], 4.5)

    def test_note_not_float(self):
        self.assertRaises(ValueError, Note, 'abc', {})
    
    def test_note_negative(self):
        self.assertRaises(ValueError, Note, 'abc', -1)
    
    def test_note_0(self):
        self.assertRaises(ValueError, Note, 'aaaaaaa', 0)

    def test_name_num(self):
        self.assertRaises(ValueError, Note, 123, 'aaaa')
    
    