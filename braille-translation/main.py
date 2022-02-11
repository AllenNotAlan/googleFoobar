from cgitb import small
from string import ascii_lowercase

def createDict(brailleLetters, brailleKey):
    unicode = [ord(elem) for elem in [char for char in ascii_lowercase]]
    for key in unicode:
        for value in brailleLetters:
            brailleKey[key] = value
            brailleLetters.remove(value)
            break

def split(word):
    return [char for char in word]

def printLetters(dict, word):
    string = ""
    word = split(word)
    for letter in word:
        letterUnicode = ord(letter)
        if letterUnicode in dict:
            string += dict[letterUnicode]
        elif ord(letter) < 97 and ord(letter) != 32:
            string += capitalCalc(dict, letterUnicode)
        else:
            string += "000000"
    return string

def capitalCalc(dict, unicode):
    letter = ""
    capital = "000001"
    neededLetter = unicode + 32
    letter = capital + dict[neededLetter]
    return letter

def solution(word):
    brailleLetters = ["100000", "110000", "100100", "100110", "100010", "110100", "110110", "110010", "010100", "010110", 
    "101000", "111000", "101100", "101110", "101010", "111100", "111110", "111010", "011100", "011110", 
    "101001", "111001", "010111", "101101", "101111", "101011"]

    brailleKey = {}
    createDict(brailleLetters= brailleLetters, brailleKey= brailleKey)

    result = printLetters(brailleKey, word)
    return result

solution("code")