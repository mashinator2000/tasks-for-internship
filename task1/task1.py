# Задание 1: круговой массив.

n, m = [int(el) for el in input().split()]

array = [i for i in range(1, n + 1)]
result = [str(1)]

p_ind = m - 1
while array[p_ind % n] != array[0]:
    result.append(str(array[p_ind % n]))
    p_ind += m - 1

print("".join(result))
