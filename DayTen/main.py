import string
import re


test = True
input = "input.txt"
testinput = "testinput.txt"
from enum import Enum

with open(testinput if test else input, "r") as f:
    lines = f.readlines()
    print(lines)