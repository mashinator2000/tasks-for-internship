# Задание 1: круговой массив.

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('n')
# parser.add_argument('m')
# args = parser.parse_args()

# n = int(args.n)
# m = int(args.m)

import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

# n, m = [int(el) for el in input().split()]

array = [i for i in range(1, n + 1)]
result = [str(1)]

p_ind = m - 1
while array[p_ind % n] != array[0]:
    result.append(str(array[p_ind % n]))
    p_ind += m - 1

print("".join(result))
