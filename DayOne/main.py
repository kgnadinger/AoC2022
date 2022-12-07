with open("input.txt", "r") as f:
    lines = f.readlines()
    
    elves = []
    topElves = []
    currentElf = 0

    for line in lines:
        if not line.strip():
            # Part 1
            elves.append(currentElf)

            # Part 2
            if len(topElves) < 3:
                topElves.append(currentElf)
            elif currentElf > min(topElves):
                topElves.remove(min(topElves))
                topElves.append(currentElf)
            currentElf = 0
        else:
            currentElf += int(line)

    print(topElves)
    print("Part 1: ", max(elves))
    print("Part 2: ", sum(topElves))

