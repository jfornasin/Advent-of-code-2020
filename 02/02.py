import re
import functools

file_object = open("advent.of.code.02.txt", "r")

rawlines = file_object.readlines()

def converttotuple(s):
    match = re.search('(\d*)-(\d*)\s(\w):\s(\w+)', s)
    return (match.group(1), match.group(2), match.group(3), match.group(4))

lines = list(map(converttotuple, rawlines))

def ispasswordvalid(passwordtuple):
    password = passwordtuple[3]
    letter = passwordtuple[2]
    first = int(passwordtuple[0])
    second = int(passwordtuple[1])

    return 1 if (password[first - 1] == letter and password[second - 1] != letter) or password[first - 1] != letter and password[second - 1] == letter else 0

result = functools.reduce(lambda a, b: a+b, list(map(ispasswordvalid, lines)))

print(result)