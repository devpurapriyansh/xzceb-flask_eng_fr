import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """
    Class to handle all testing of the English to French translator
    """
    def test1(self):
        """Test the basic 'Hello' greeting"""
        self.assertEqual(english_to_french('Hello'), 'Bonjour')



class TestFrenchToEnglish(unittest.TestCase):
    """
    Class to handle testing of the French To English translator
    """
    def test1(self):
        """Test the basic 'Hello' greeting"""
        self.assertEqual(french_to_english('Bonjour'), 'Hello')


unittest.main()