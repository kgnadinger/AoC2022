import string

test = False
input = "input.txt"
testinput = "testinput.txt"

with open(testinput if test else input, "r") as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

    pairs = 0
    secondPairs = 0
    for line in lines:
        split = line.split(",")
        firstElf = split[0]
        secondElf = split[1]

        e1 = int(firstElf.split('-')[0])
        e2 = int(firstElf.split('-')[1])

        e3 = int(secondElf.split('-')[0])
        e4 = int(secondElf.split('-')[1])

        if e1 <= e3 and e2 >= e4 or e3 <= e1 and e4 >= e2:
            pairs += 1

        if (e2 != e3) and (e1 < e3 and e2 < e4 and e2 < e3) or (e3 < e1 and e4 < e1 and e3 < e2):
            print(f"({e1}-{e2}), ({e3}-{e4})")
            secondPairs += 1

    print("Part 1: ", pairs)
    print("Part 2: ", len(lines) - secondPairs)        