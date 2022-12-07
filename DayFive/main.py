import string
import re

test = False
input = "input.txt"
testinput = "testinput.txt"

with open(testinput if test else input, "r") as f:
    lines = list(map(lambda x: x.strip("\n"), f.readlines()))
    inputCrates = {}
    crates = {}
    partTwoCrates = {}
    exitLoop = False
    for line in lines:
        for index, char in enumerate(line):
            if exitLoop:
                break
            if char == "1":
                exitLoop = True
                break
            if char in string.ascii_letters:
                if index in inputCrates.keys():
                    inputCrates[index].append(char)
                else:
                    inputCrates[index] = [char]
    
    i = 1
    for key in sorted(inputCrates.keys()):
        crates[i] = inputCrates[key]
        partTwoCrates[i] = inputCrates[key].copy()
        i += 1

    # Part 1
    for line in lines:
        if line == "" or line[0] != "m":
            continue
        inputs = re.split(r'move|from|to', line)
        inputs.pop(0)
        inputs = list(map(lambda x: int(x), inputs))
        
        for i in range(inputs[0]):
            crate = crates[inputs[1]].pop(0)
            crates[inputs[2]].insert(0, crate)
    
    answerString = ""
    for key in sorted(crates.keys()):
        answerString += crates[key][0]

    # Part 2
    for line in lines:
        if line == "" or line[0] != "m":
            continue
        inputs = re.split(r'move|from|to', line)
        inputs.pop(0)
        inputs = list(map(lambda x: int(x), inputs))

        slice = partTwoCrates[inputs[1]][0:int(inputs[0])]
        for index, char in enumerate(slice):
            partTwoCrates[inputs[2]].insert(index, char)
            partTwoCrates[inputs[1]].remove(char)
    
    partTwoAnswer = ""
    for key in sorted(partTwoCrates.keys()):
        partTwoAnswer += partTwoCrates[key][0]

    print("Part 1 Crates: ", answerString)
    print("Part 2 crates: ", partTwoAnswer)
        
        