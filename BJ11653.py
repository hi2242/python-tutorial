import sys

input = sys.stdin.readline

N = int(input())
i = 3
A = []

while N % 2 == 0:
    N = N // 2
    A.append(2)

while True:
    if N == 1:
        break
    
    elif N == i:
        A.append(i)
        break

    elif N % i == 0:
        N = N // i
        A.append(i)

    else:
        i += 2

print(*A, sep = "\n")