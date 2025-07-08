# Задание 4: приближение чисел к одному в массиве

file = input()

array = []

with open(file, 'r') as file:
    a = file.readline().strip()
    while a:
        array.append(int(a))
        a = file.readline().strip()

# array = [1, 9, 2, 10]
array.sort()
step = 0
avg_el = len(array) // 2

for el in array:
    while el != avg_el:
        if el < avg_el:
            el += 1
        else:
            el -= 1
        step += 1

print(step)

