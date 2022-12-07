import string
import re

test = False
input = "input.txt"
testinput = "testinput.txt"

with open(testinput if test else input, "r") as f:
    line = f.read()
    
    letters = []
    position = 0

    partTwoLetters = []
    partTwoPosition = 0

    for index, char in enumerate(line):
        # Part 1
        if len(letters) < 4 and char not in letters:
            letters.append(char)
            if len(letters) == 4:
                position = index + 1
                break
        elif len(letters) < 4 and char in letters:
            letters = letters[letters.index(char)+1:]
            letters.append(char)

    for index, char in enumerate(line):
        # Part 2
        print("Part 2 Letters: ", partTwoLetters)
        if len(partTwoLetters) < 14 and char not in partTwoLetters:
            partTwoLetters.append(char)
            if len(partTwoLetters) == 14:
                partTwoPosition = index + 1
                break
        elif len(partTwoLetters) < 14 and char in partTwoLetters:
            partTwoLetters = partTwoLetters[partTwoLetters.index(char)+1:]
            partTwoLetters.append(char)

    
    print("Part 1: ", position)
    print("Part 2: ", partTwoPosition)
            
        