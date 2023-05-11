
import unittest
from unittester1 import IsPalindrom
class TestIsPalindrom(unittest.TestCase):
    def test_empty_string(self):
     #assert   
        self.assertTrue(IsPalindrom(""))

    def test_single_character_string(self):
      #assert  
        self.assertTrue(IsPalindrom("a"))

    def test_palindromic_string(self):
     #assert   
        self.assertTrue(IsPalindrom("racecar"))

    def test_non_palindromic_string(self):
    #assert    
        self.assertFalse(IsPalindrom("not a palindrome"))

    def test_string_with_spaces(self):
        self.assertTrue(IsPalindrom("A man a plan a canal Panama"))

    def test_string_with_punctuation(self):
     #assert   
        self.assertTrue(IsPalindrom("Was it a car or a cat I saw?"))

    def test_string_with_mixed_case(self):
      #assert  
        self.assertTrue(IsPalindrom("Madam In Eden, I'm Adam"))

if __name__ == '__main__':
    unittest.main()