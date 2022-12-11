import string
import re
import math
from itertools import chain


test = False
input = "input.txt"
testinput = "testinput.txt"
from enum import Enum


with open(testinput if test else input, "r") as f:
    lines = f.readlines()

    monkeys = []
        # monkey = {
        #     "items": [],
        #     "operationAmount": 19, # can be old
        #     "operation": "add",
        #     "test": 23,
        #     "ifTrue": 2,
        #     "ifFalse": 3
        # }
    currentMonkey = {}

    for line in lines:
        cleanLine = line.strip("\n").strip()
        splitString = cleanLine.split(": ")
        if "Monkey" in splitString[0]:
            if len(currentMonkey.keys()) > 0:
                monkeys.append(currentMonkey)
            id = splitString[0].split(" ")[1].split(":")[0]
            currentMonkey = { "id": int(id), "inspected": 0 }
        elif splitString[0] == "Starting items":
            itemList = list(map(lambda x: int(x), splitString[1].split(", ")))
            currentMonkey["items"] = itemList
        elif splitString[0] == "Test":
            splitTest = splitString[1].split(" ")
            currentMonkey["test"] = int(splitTest[2])
        elif splitString[0] == "If true":
            monkeyTrueString = splitString[1].split(" ")
            whichMonkey = int(monkeyTrueString[len(monkeyTrueString)-1])
            currentMonkey["ifTrue"] = whichMonkey
        elif splitString[0] == "If false":
            monkeyTrueString = splitString[1].split(" ")
            whichMonkey = int(monkeyTrueString[len(monkeyTrueString)-1])
            currentMonkey["ifFalse"] = whichMonkey
        elif splitString[0] == "Operation":
            operationString = splitString[1].split("new = old ")
            operationType = operationString[1].split(" ")[0]
            operationAmount = operationString[1].split(" ")[1]
            currentMonkey["operationAmount"] = operationAmount
            currentMonkey["operation"] = operationType
    monkeys.append(currentMonkey)
    
    def runSimulation(monkeys):
        for round in range(20):
            print("*************", round)
            for monkey in monkeys:
                while len(monkey["items"]) > 0:
                    monkey["inspected"] += 1
                    item = monkey["items"].pop(0)
                    amount = monkey["operationAmount"] if monkey["operationAmount"].isnumeric() else item
                    match monkey["operation"]:
                        case "+":
                            item += int(amount)
                        case "*":
                            item *= int(amount)
                    item = item // 3
                    if item % monkey["test"] == 0:
                        monkeys[monkey["ifTrue"]]["items"].append(item)
                    else:
                        monkeys[monkey["ifFalse"]]["items"].append(item)
        return monkeys

    def primeFactors(n):
        primes = []
        if n == 2:
            return [2]
        while n % 2 == 0:
            if n not in primes:
                primes.append(2)
            n = n / 2
            
        # n must be odd at this point
        # so a skip of 2 ( i = i + 2) can be used
        for i in range(3,int(math.sqrt(n))+1,2):
            # while i divides n , print i and divide n
            while n % i== 0:
                if i not in primes:
                    primes.append(i)
                n = n / i
        
        if len(primes) == 0:
            return [n]
        return primes
    
    def mod(item, a):
        currentOperation = None
        operations = ["+", "*", "**"]
        currentMod = None

        for i in item:
            if i == "**":
                currentMod = (currentMod * currentMod) % a
                currentOperation = None
            elif i in operations:
                currentOperation = i
            elif currentOperation is None:
                currentMod = i % a
            else:
                if currentOperation == "+":
                    currentMod = (currentMod + (i % a)) % a
                elif currentOperation == "*":
                    currentMod = (currentMod * (i % a)) % a
        return currentMod


                
    def runSecondSimulation():
        monkeys = []
        # monkey = {
        #     "items": [],
        #     "operationAmount": 19, # can be old
        #     "operation": "add",
        #     "test": 23,
        #     "ifTrue": 2,
        #     "ifFalse": 3
        # }
        currentMonkey = {}

        for line in lines:
            cleanLine = line.strip("\n").strip()
            splitString = cleanLine.split(": ")
            if "Monkey" in splitString[0]:
                if len(currentMonkey.keys()) > 0:
                    monkeys.append(currentMonkey)
                id = splitString[0].split(" ")[1].split(":")[0]
                currentMonkey = { "id": int(id), "inspected": 0 }
            elif splitString[0] == "Starting items":
                itemList = list(map(lambda x: [int(x)], splitString[1].split(", ")))
                currentMonkey["items"] = itemList
            elif splitString[0] == "Test":
                splitTest = splitString[1].split(" ")
                currentMonkey["test"] = int(splitTest[2])
            elif splitString[0] == "If true":
                monkeyTrueString = splitString[1].split(" ")
                whichMonkey = int(monkeyTrueString[len(monkeyTrueString)-1])
                currentMonkey["ifTrue"] = whichMonkey
            elif splitString[0] == "If false":
                monkeyTrueString = splitString[1].split(" ")
                whichMonkey = int(monkeyTrueString[len(monkeyTrueString)-1])
                currentMonkey["ifFalse"] = whichMonkey
            elif splitString[0] == "Operation":
                operationString = splitString[1].split("new = old ")
                operationType = operationString[1].split(" ")[0]
                operationAmount = operationString[1].split(" ")[1]
                currentMonkey["operationAmount"] = operationAmount
                currentMonkey["operation"] = operationType
        monkeys.append(currentMonkey)
        for round in range(10000):
            if round % 1000 == 0:
                print("*************", round)
            for monkey in monkeys:
                while len(monkey["items"]) > 0:
                    monkey["inspected"] += 1
                    item = monkey["items"].pop(0)
                    if monkey["operationAmount"].isnumeric():
                        operation = monkey["operation"]
                        item.append(operation)
                        item.append(int(monkey["operationAmount"]))
                    else:
                        item.append("**")
                    if mod(item, monkey["test"]) == 0:
                        monkeys[monkey["ifTrue"]]["items"].append(item)
                    else:
                        monkeys[monkey["ifFalse"]]["items"].append(item)
        return monkeys
        
    print("Problem 1: ", list(map(lambda x: x["inspected"], runSimulation(monkeys.copy()))))
    print("Problem 2: ", list(map(lambda x: x["inspected"], runSecondSimulation())))
