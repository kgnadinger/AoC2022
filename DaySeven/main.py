import string
import re

test = False
input = "input.txt"
testinput = "testinput.txt"

def printFileSystem(filesystem, lvl=1):
        for key in filesystem.keys():
            dash = "-" * lvl
            if isinstance(filesystem[key], dict):
                print(f"{dash} {key} (dir)")
                printFileSystem(filesystem[key], lvl + 1)
            else:
                print(f"{dash} {key} (file, size={filesystem[key]})")

with open(testinput if test else input, "r") as f:
    lines = f.readlines()

    filesystem = {"/": {}}

    def insertFile(file, path, filesystem):
        # print(f"Insert {file} into {path} in {printFileSystem(filesystem)}")
        if len(path) == 0:
            filesystem[file["name"]] = file["size"]
        else:
            keyPath = path.split(".")
            key = keyPath.pop(0)
            newPath = ".".join(keyPath)
            insertFile(file, newPath, filesystem[key])

    def insertDir(dir, path, filesystem):
        # print(f"Insert {dir} into {path} in {printFileSystem(filesystem)}")
        if len(path) == 0:
            filesystem[dir] = {}
        else:
            keyPath = path.split(".")
            key = keyPath.pop(0)
            newPath = ".".join(keyPath)
            insertDir(dir, newPath, filesystem[key])

    pwd = ""

    for line in lines:
        cleanLine = line.strip("\n")
        command = cleanLine.split(" ")
        # print(f"Command {command}, pwd: {pwd}")
        # printFileSystem(filesystem)
        if command[0] == "$":
            if command[1] == "cd":
                if command[2] == "/":
                    pwd = command[2]
                elif command[2] == "..":
                    pwdList = pwd.split(".")
                    pwdList = pwdList[0:len(pwdList)-1]
                    pwd = ".".join(pwdList)
                else:
                    pwd += f".{command[2]}"
        else:
            # print("$ ", command, pwd)
            if command[0].isnumeric():
                file = {
                    "name": command[1],
                    "size": command[0]
                }
                insertFile(file, pwd, filesystem)
            else:
                insertDir(command[1], pwd, filesystem)

    def findSumOfDir(filesystem):
        size = 0
        for key in filesystem.keys():
            if isinstance(filesystem[key], dict):
                size += findSumOfDir(filesystem[key])
            else:
                size += int(filesystem[key])
        return size

    # printFileSystem(filesystem)

    def findSumOfDirectoriesLessThan(amount, filesystem):
        size = 0
        for key in filesystem.keys():
            if isinstance(filesystem[key], dict):
                sum = findSumOfDir(filesystem[key])
                if sum <= amount:
                    size += sum
                size += findSumOfDirectoriesLessThan(amount, filesystem[key])
        return size

    def findDirectoryToDelete(amount, filesystem):
        directories = []
        for key in filesystem.keys():
            if isinstance(filesystem[key], dict):
                size = findSumOfDir(filesystem[key])
                if size >= leastAmountOfSpaceToDelete:
                    directories.append(size)
                for dir in findDirectoryToDelete(amount, filesystem[key]):
                    directories.append(dir)
        return directories

    sumTopDir = findSumOfDir(filesystem)
    unusedSpace = 70000000 - sumTopDir
    leastAmountOfSpaceToDelete = 30000000 - unusedSpace

    print(f"Part 1: {findSumOfDirectoriesLessThan(100000, filesystem)}")
    print(f"Part 2: {min(findDirectoryToDelete(leastAmountOfSpaceToDelete, filesystem))}")