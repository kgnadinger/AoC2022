import string
import re


test = False
input = "input.txt"
testinput = "testinput.txt"
from enum import Enum

with open(testinput if test else input, "r") as f:
    lines = f.readlines()

    def problemOne():
        currentHeadPosition = { "x": 0, "y": 0 }
        currentTailPosition = { "x": 0, "y": 0 }
        visits = [{"x": 0, "y": 0 }]

        def isTailClose():
            xDiff = abs(currentHeadPosition["x"] - currentTailPosition["x"])
            yDiff = abs(currentHeadPosition["y"] - currentTailPosition["y"])
            return xDiff <= 1 and yDiff <= 1

        for line in lines:
            cleanLine = line.strip("\n")
            direction, amountString = cleanLine.split()
            amount = int(amountString)
            for n in range(amount):
                if not isTailClose():
                    if currentHeadPosition["x"] == currentTailPosition["x"]:
                        if currentHeadPosition["y"] - currentTailPosition["y"] > 0:
                            currentTailPosition["y"] += 1
                        else:
                            currentTailPosition["y"] -= 1
                    elif currentHeadPosition["y"] == currentTailPosition["y"]:
                        if currentHeadPosition["x"] - currentTailPosition["x"] > 0:
                            currentTailPosition["x"] += 1
                        else:
                            currentTailPosition["x"] -= 1
                    else:
                        if currentHeadPosition["x"] - currentTailPosition["x"] > 0:
                            currentTailPosition["x"] += 1
                        else:
                            currentTailPosition["x"] -= 1
                        if currentHeadPosition["y"] - currentTailPosition["y"] > 0:
                            currentTailPosition["y"] += 1
                        else:
                            currentTailPosition["y"] -= 1
                match direction:
                    case "U":
                        currentHeadPosition["y"] += 1
                    case "D":
                        currentHeadPosition["y"] -= 1
                    case "L":
                        currentHeadPosition["x"] -= 1
                    case "R":
                        currentHeadPosition["x"] += 1
                if currentTailPosition not in visits:
                    visits.append(currentTailPosition.copy())
        if not isTailClose():
            if currentHeadPosition["x"] == currentTailPosition["x"]:
                if currentHeadPosition["y"] - currentTailPosition["y"] > 0:
                    currentTailPosition["y"] += 1
                else:
                    currentTailPosition["y"] -= 1
            elif currentHeadPosition["y"] == currentTailPosition["y"]:
                if currentHeadPosition["x"] - currentTailPosition["x"] > 0:
                    currentTailPosition["x"] += 1
                else:
                    currentTailPosition["x"] -= 1
            else:
                if currentHeadPosition["x"] - currentTailPosition["x"] > 0:
                    currentTailPosition["x"] += 1
                else:
                    currentTailPosition["x"] -= 1
                if currentHeadPosition["y"] - currentTailPosition["y"] > 0:
                    currentTailPosition["y"] += 1
                else:
                    currentTailPosition["y"] -= 1
            if currentTailPosition not in visits:
                    visits.append(currentTailPosition.copy())
        print("Part 1: ", len(visits))
    
    def problemTwo():
        currentHeadPosition = { "x": 0, "y": 0 }
        currentTailPositions = [
            { "x": 0, "y": 0 },
            { "x": 0, "y": 0 },
            { "x": 0, "y": 0 },
            { "x": 0, "y": 0 },
            { "x": 0, "y": 0 },
            { "x": 0, "y": 0 },
            { "x": 0, "y": 0 },
            { "x": 0, "y": 0 },
            { "x": 0, "y": 0 }
        ]
        visits = [{"x": 0, "y": 0 }]

        def isTailClose(head, tail):
            xDiff = abs(head["x"] - tail["x"])
            yDiff = abs(head["y"] - tail["y"])
            return xDiff <= 1 and yDiff <= 1

        for line in lines:
            cleanLine = line.strip("\n")
            direction, amountString = cleanLine.split()
            amount = int(amountString)
            for n in range(amount):
                i = 8
                while i >= 0:
                    head = currentHeadPosition
                    tail = currentTailPositions[i]
                    if i != 8:
                        head = currentTailPositions[i+1]
                    if not isTailClose(head, tail):
                        if head["x"] == tail["x"]:
                            if head["y"] - tail["y"] > 0:
                                tail["y"] += 1
                            else:
                                tail["y"] -= 1
                        elif head["y"] == tail["y"]:
                            if head["x"] - tail["x"] > 0:
                                tail["x"] += 1
                            else:
                                tail["x"] -= 1
                        else:
                            if head["x"] - tail["x"] > 0:
                                tail["x"] += 1
                            else:
                                tail["x"] -= 1
                            if head["y"] - tail["y"] > 0:
                                tail["y"] += 1
                            else:
                                tail["y"] -= 1
                        if currentTailPositions[0] not in visits:
                            visits.append(currentTailPositions[0].copy())
                    i -= 1
                match direction:
                    case "U":
                        currentHeadPosition["y"] += 1
                    case "D":
                        currentHeadPosition["y"] -= 1
                    case "L":
                        currentHeadPosition["x"] -= 1
                    case "R":
                        currentHeadPosition["x"] += 1
        print("Part 2: ", len(visits)+1)
        # for t in range(9):
        #     head = currentHeadPosition
        #     tail = currentTailPositions[t]
        #     if t != 8:
        #         head = currentTailPositions[t+1]
        #     if not isTailClose(head, tail):
        #         if head["x"] == currentTailPositions[t]["x"]:
        #             if head["y"] - currentTailPositions[t]["y"] > 0:
        #                 currentTailPositions[t]["y"] += 1
        #             else:
        #                 currentTailPositions[t]["y"] -= 1
        #         elif head["y"] == currentTailPositions[t]["y"]:
        #             if head["x"] - currentTailPositions[t]["x"] > 0:
        #                 currentTailPositions[t]["x"] += 1
        #             else:
        #                 currentTailPositions[t]["x"] -= 1
        #         else:
        #             if head["x"] - currentTailPositions[t]["x"] > 0:
        #                 currentTailPositions[t]["x"] += 1
        #             else:
        #                 currentTailPositions[t]["x"] -= 1
        #             if head["y"] - currentTailPositions[t]["y"] > 0:
        #                 currentTailPositions[t]["y"] += 1
        #             else:
        #                 currentTailPositions[t]["y"] -= 1
        #         break
        #     if currentTailPositions[0] not in visits:
        #         visits.append(currentTailPositions[0].copy())
        # print("Part 2: ", visits)

    problemOne()
    problemTwo()