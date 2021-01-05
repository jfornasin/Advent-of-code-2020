file_object = open("advent.of.code.01.txt", "r")
lines = file_object.readlines()

numbers = list(map(int, lines))

result = [(x, y, z) for x in numbers for y in numbers for z in numbers if x+y+z == 2020]

print(result[0][0]*result[0][1]*result[0][2])
