# 1. Skapa automatiska enhetstester för IsPalindrom
# - ta din egen eller denna
# def IsPalindrom(input):
#     s = input.replace(" ", "").lower()
#     backwards = ""
#     for part in s:
#         backwards = part + backwards

#     return backwards == s
import unittest

# class TestIsPalindrom(unittest.TestCase):
    
#     def test_single_word_palindrom(self):
#         self.assertTrue(IsPalindrom("racecar"))
        
#     def test_single_word_non_palindrom(self):
#         self.assertFalse(IsPalindrom("apple"))
        
#     def test_phrase_palindrom(self):
#         self.assertTrue(IsPalindrom("A man a plan a canal Panama"))
        
#     def test_phrase_non_palindrom(self):
#         self.assertFalse(IsPalindrom("This is not a palindrom"))
        
#     def test_palindrom_with_spaces(self):
#         self.assertTrue(IsPalindrom("never odd or even"))
        
#     def test_palindrom_with_punctuation(self):
#         self.assertTrue(IsPalindrom("Able was I, ere I saw Elba!"))
        
# if __name__ == '__main__':
#     unittest.main()
def IsPalindrom(input):
    s = input.replace(" ", "").lower()
    backwards = ""
    for part in s:
        backwards = part + backwards

    return backwards == s
