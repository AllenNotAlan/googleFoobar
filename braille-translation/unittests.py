import unittest
import main

class TestStringMethods(unittest.TestCase):

    def test_word(self):
        self.assertEqual(main.solution("code"), "100100101010100110100010")

    def test_word_with_capitals(self):
        self.assertEqual(main.solution("Braille"), "000001110000111010100000010100111000111000100010")
        
    def test_sentence(self):
        self.assertEqual(main.solution("The quick brown fox jumps over the lazy dog"),
         "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110")

if __name__ == '__main__':
    unittest.main()