import string
import re


test = False
input = "input.txt"
testinput = "testinput.txt"
from enum import Enum

with open(testinput if test else input, "r") as f:
    lines = f.readlines()
    
    cycle = 1
    x = 1
    toBeAdded = None
    interesting = [20, 60, 100, 140, 180, 220]
    sum = 0
    screen = ""

    def isSpritePresent():
        sprite = [x-1, x, x+1]
        return (cycle - 1) % 40 in [x-1, x, x+1]

    for line in lines:
        cleanLine = line.strip("\n")
        instructionString = cleanLine.split()
        instruction = instructionString[0]
        amount = 0
        if len(instructionString) > 1:
            amount = int(instructionString[1])

        if instruction == "noop":
            if cycle in interesting:
                sum += cycle * x
            if isSpritePresent():
                screen += "#"
            else:
                screen += "."
            if cycle % 40 == 0:
                screen += "\n"
            cycle += 1
        else:
            for n in range(2):
                if cycle in interesting:
                    sum += cycle * x
                if isSpritePresent():
                    screen += "#"
                else:
                    screen += "."
                if cycle % 40 == 0:
                    screen += "\n"
                cycle += 1  
                if n == 1:
                    x += amount



    print(sum)
    print(screen)