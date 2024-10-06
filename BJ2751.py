import sys

input = sys.stdin.readline

plusList = [False] * 1000001
minusList = [False] * 1000000

N = int(input())

for _ in range(N):
    A = int(input())
    if A >= 0:
        plusList[A] = True
    else:
        minusList[abs(A + 1)] = True

for i in range(1000000, 0, -1):
    if N == 0:
        break
    elif minusList[i - 1] == True:
        print("-", i, sep = "")
        N -= 1
    else:
        continue

for i in range(1000001):
    if N == 0:
        break
    elif plusList[i] == True:
        print(i)
        N -= 1
    else:
        continue