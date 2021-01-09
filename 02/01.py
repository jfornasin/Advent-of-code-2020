import re
import functools
# # import inspect
# # import os

# # scriptFileName = inspect.getframeinfo(inspect.currentframe()).filename
# # path = os.path.dirname(os.path.abspath(scriptFileName))
# # files = os.listdir()

file_object = open("advent.of.code.02.txt", "r")

rawlines = file_object.readlines()

def converttotuple(s):
    match = re.search('(\d*)-(\d*)\s(\w):\s(\w+)', s)
    return (match.group(1), match.group(2), match.group(3), match.group(4))

lines = list(map(converttotuple, rawlines))

def ispasswordvalid(passwordtuple):
    password = passwordtuple[3]
    letter = passwordtuple[2]
    lowestnum = passwordtuple[0]
    highestnum = passwordtuple[1]

    repetitions = password.count(letter)
    return 1 if (repetitions >= int(lowestnum)) and (repetitions <= int(highestnum)) else 0

result = functools.reduce(lambda a, b: a+b, list(map(ispasswordvalid, lines)))

print(result)