# Задание 2: окружность и точки

file1, file2 = [el for el in input().split()]

with open(file1, 'r') as file:
    center = [int(el) for el in file.readline().split()]
    r = int(file.readline())

point = []
with open(file2, 'r') as file:
    p = file.readline().strip()
    while p:
        point.append([int(el) for el in p.split()])
        p = file.readline().strip()



def point_in_circle(point, center, r):
    S = (point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2

    if S < r ** 2:
        return 1
    elif S == r ** 2:
        return 0
    else:
        return 2

for el in point:
    print(point_in_circle(el, center, r))


