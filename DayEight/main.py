import string
import re
import functools


test = False
input = "input.txt"
testinput = "testinput.txt"

with open(testinput if test else input, "r") as f:
    lines = f.readlines()
    t = {}
    s = []
    tallYAbove = [-1] * len(lines[0])
    tallYBelow = [-1] * len(lines[0])

    for y, line in enumerate(lines):
        trees = list(map(lambda x: int(x), line.strip("\n")))
        tallXLeft = -1
        tallXRight = -1
        for x, tree in enumerate(trees):
            #Part 1

            #left
            if tree > tallXLeft:
                tallXLeft = tree
                if x in t.keys():
                    t[x][y] = True
                else:
                    t[x] = { y: True }

            #above
            if tree > tallYAbove[x]:
                tallYAbove[x] = tree
                if x in t.keys():
                    t[x][y] = True
                else:
                    t[x] = { y: True }

            #right
            rTree = trees[-(x+1)]
            if rTree > tallXRight:
                tallXRight = rTree
                index = len(trees) - (x+1)
                if index in t.keys():
                    t[index][y] = True
                else:
                    t[index] = { y: True }
            
            #below
            oppositeIndex = len(lines)-1-y
            oppositeLine = lines[oppositeIndex]
            bTree = int(oppositeLine[x])
            if bTree > tallYBelow[x]:
                tallYBelow[x] = bTree
                if x in t.keys():
                    t[x][oppositeIndex] = True
                else:
                    t[x] = { oppositeIndex: True }


            # Part 2
            scenics = []
            #left
            i = x - 1
            currentHeight = -1
            treeAmount = 0
            leftViewIsBlocked = False
            while i >= 0:
                if not leftViewIsBlocked and trees[i] >= trees[x]:
                    leftViewIsBlocked = True
                    treeAmount += 1
                # elif not leftViewIsBlocked and trees[i] >= currentHeight:
                #     treeAmount += 1
                #     currentHeight = trees[i]
                elif not leftViewIsBlocked:
                    treeAmount += 1
                i -= 1
            scenics.append(treeAmount)

            #right
            i = x + 1
            currentRightHeight = -1
            rightTreeAmount = 0
            rightViewIsBlocked = False
            while i <= len(trees) - 1:
                if not rightViewIsBlocked and trees[i] >= trees[x]:
                    rightViewIsBlocked = True
                    rightTreeAmount += 1
                # elif not rightViewIsBlocked and trees[i] >= currentRightHeight:
                #     currentRightHeight = trees[i]
                #     rightTreeAmount += 1
                elif not rightViewIsBlocked:
                    rightTreeAmount += 1
                i += 1
            scenics.append(rightTreeAmount)

            #up
            i = y - 1
            currentUpHeight = -1
            upTreeAmount = 0
            upViewIsBlocked = False
            while i >= 0:
                tree = int(lines[i][x])
                if not upViewIsBlocked and tree >= trees[x]:
                    upViewIsBlocked = True
                    upTreeAmount += 1
                # elif not upViewIsBlocked and tree >= currentUpHeight:
                #     currentUpHeight = tree
                #     upTreeAmount += 1
                elif not upViewIsBlocked:
                    upTreeAmount += 1
                i -= 1
            scenics.append(upTreeAmount)

            #down
            i = y + 1
            currentDownHeight = -1
            downTreeAmount = 0
            downViewIsBlocked = False
            while i <= len(lines) - 1:
                tree = int(lines[i][x])
                if not downViewIsBlocked and tree >= trees[x]:
                    downViewIsBlocked = True
                    downTreeAmount += 1
                # elif not downViewIsBlocked and tree >= currentDownHeight:
                #     currentDownHeight = tree
                #     downTreeAmount += 1
                elif not downViewIsBlocked:
                    downTreeAmount += 1
                i += 1
            scenics.append(downTreeAmount)

            score = functools.reduce(lambda a, b: a*b, scenics)
            # print(f"Tree: {x}, {y}", scenics, score)
            s.append(score)

    sum = 0
    for x in t.keys():
        for y in t[x].keys():
            sum += 1

    
    print("Part 1: ", sum)
    print("Part 2: ", max(s))
            

             

            

                
                
            

