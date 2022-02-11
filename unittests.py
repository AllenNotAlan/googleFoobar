import unittest
import brailleSolution
import powerHungrySolution

class TestStringMethods(unittest.TestCase):

    def test_word(self):
        self.assertEqual(brailleSolution.solution("code"), "100100101010100110100010")

    def test_word_with_capitals(self):
        self.assertEqual(brailleSolution.solution("Braille"), "000001110000111010100000010100111000111000100010")
        
    def test_sentence(self):
        self.assertEqual(brailleSolution.solution("The quick brown fox jumps over the lazy dog"),
         "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110")

    def test_power_five_panel(self):
        testList = [2, 0, 2, 2, 0]
        self.assertEqual(powerHungrySolution.solution(testList), str(8))

    def test_power_always_positive(self):
        testList = [-2,-3, 4,-5]
        self.assertEqual(powerHungrySolution.solution(testList), str(60))

if __name__ == '__main__':
    unittest.main()