import unittest
from machinetranslation.translator import english_to_french, french_to_english

class TestTranslation(unittest.TestCase):
    
    def test_english_to_french(self):
        # Test for valid input
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("How are you"), "Bonjour")
        
        # Test for empty input
        self.assertEqual(english_to_french(""), "")
        
    def test_french_to_english(self):
        # Test for valid input
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Comment allez-vous ?"), "Hello")
      
        # Test for empty input
        self.assertEqual(french_to_english(""), "")
        
if __name__ == '__main__':
    unittest.main()