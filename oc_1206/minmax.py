numbers = [1, 100, -1, 30, 5, 99, 45, 39, -2, -10]
max = numbers[0]

for number in numbers:
     if number > max:
         max = number

print("최대값은" + str(max))