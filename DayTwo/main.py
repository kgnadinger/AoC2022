test = False
input = "input.txt"
testinput = "testinput.txt"
with open(testinput if test else input, "r") as f:
    lines = f.readlines()

    playScore = {
        "A": 1, #rock
        "B": 2, #paper
        "C": 3, #scissors
        "X": 1, #rock
        "Y": 2, #paper
        "Z": 3  #scissors
    } 

    def isWin(opp, min):        
        if opp == "A" and mine == "X":
            return "tie"
        if opp == "A" and mine == "Y":
            return "win"
        if opp == "A" and mine == "Z":
            return "loss"
        if opp == "B" and mine == "X":
            return "loss"
        if opp == "B" and mine == "Y":
            return "tie"
        if opp == "B" and mine == "Z":
            return "win"
        if opp == "C" and mine == "X":
            return "win"
        if opp == "C" and mine == "Y":
            return "loss"
        if opp == "C" and mine == "Z":
            return "tie"
    
    def findScore(opp, outcome):
        if opp == "A" and mine == "X":
            return playScore["Z"] + 0
        if opp == "A" and mine == "Y":
            return playScore["X"] + 3
        if opp == "A" and mine == "Z":
            return playScore["Y"] + 6
        if opp == "B" and mine == "X":
            return playScore["X"] + 0
        if opp == "B" and mine == "Y":
            return playScore["Y"] + 3
        if opp == "B" and mine == "Z":
            return playScore["Z"] + 6
        if opp == "C" and mine == "X":
            return playScore["Y"] + 0
        if opp == "C" and mine == "Y":
            return playScore["Z"] + 3
        if opp == "C" and mine == "Z":
            return playScore["X"] + 6

    score = 0
    newScore = 0
    for line in lines:
        cleanLine = line.strip()
        plays = cleanLine.split(" ")
        opp = plays[0]
        mine = plays[1]
        
        oppScore = playScore[opp]
        myScore = playScore[mine]

        if isWin(opp, mine) == "win":
            score += myScore + 6
        elif isWin(opp, mine) == "loss":
            score += myScore
        else:
            score += myScore + 3
        newScore += findScore(opp, mine)

        
    
    print("Part 1: ", score)
    print("Part 2: ", newScore)