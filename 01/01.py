file_object = open("advent.of.code.01.txt", "r")
lines = file_object.readlines()

numbers = list(map(int, lines))

result = [(num1, num2) for num1 in numbers for num2 in numbers if num1+num2 == 2020]

print(result[0][0]*result[0][1])
