import string

test = False
input = "input.txt"
testinput = "testinput.txt"
with open(testinput if test else input, "r") as f:
    lines = f.readlines()

    def score(char):
        lowerAlphabet = list(string.ascii_lowercase)
        upperAlphabet = list(string.ascii_uppercase)
        if char in lowerAlphabet:
            return lowerAlphabet.index(char) + 1
        if char in upperAlphabet:
            return (upperAlphabet.index(char) + 1) + 26
    
    currentSack = []
    errorStack = []
    errorScore = 0

    badgeScore = 0
    badges = []

    currentElfGroup = []
    for line in lines:
        cleanLine = line.strip()

        # Part 1
        lineLength = len(cleanLine)
        for index, char in enumerate(cleanLine):
            if index < (len(cleanLine) / 2):
                currentSack.append(char)
            elif char in currentSack and char not in errorStack:
                errorStack.append(char)
                errorScore += score(char)
            if index == len(cleanLine) - 1:
                currentSack = []
                errorStack = []

        # Part 2
        if len(currentElfGroup) == 2:
            currentElfGroup.append(cleanLine)
            listLengths = list(map(lambda x: len(x), currentElfGroup))
            listLengthMax = max(listLengths)
            listLengthMaxIndex = listLengths.index(listLengthMax)

            for char in currentElfGroup[listLengthMaxIndex]:
                if char in currentElfGroup[0] and char in currentElfGroup[1] and char in currentElfGroup[2] and char not in badges:
                    badges.append(char)
                    badgeScore += score(char)
            
            currentElfGroup = []
            badges = []
        else:
            currentElfGroup.append(cleanLine)
        
    
    print("Part 1: ", errorScore)
    print("Part 2: ", badgeScore)



            