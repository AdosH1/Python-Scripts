#A unit test for my function linebreak in linebreaker.py
# By Aden Huen

from linebreaker import *
import unittest

class test_linebreak(unittest.TestCase):
        
    #testing width values pos+, neg- and 0
    def test_zero_width(self):
        self.assertEqual(linebreak("The quick fox jumped over the lazy sleeping dog.", 0), 'The line break length is too small.')
        
    def test_negative_width(self):
        self.assertEqual(linebreak("The quick fox jumped over the lazy sleeping dog.", -15), 'The line break length is too small.')
        
    def test_great_width(self):
        self.assertIsNone(linebreak("The quick fox jumped over the lazy sleeping dog.", 5000))
    
    #test width that is smaller than the number of characters in the longest word
    def test_small_width(self):
        self.assertEqual(linebreak("The quick fox jumped over the lazy sleeping dog.", 5), 'The line break length is too small.')
    
    #testing of a non-string entered in function
    def test_non_string(self):
        self.assertEqual(linebreak(1502, 15), 'Please enter valid arguments.')
    
    #testing of a not integer for width
    def test_non_int(self):
        self.assertEqual(linebreak("The quick fox jumped over the lazy sleeping dog.", 'Mac the Car Jack'), 'Please enter valid arguments.')
    
    #attempt integer overflow
    def test_overflow_width(self):
        self.assertIsNone(linebreak("The quick fox jumped over the lazy sleeping dog.", 999999999999))
        
if __name__ == "__main__":
    unittest.main()