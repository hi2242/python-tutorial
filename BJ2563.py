import sys

input = sys.stdin.readline

num = int(input())

whole = [[0] * 100 for _ in range(100)]
ar = 0

xy = []

for i in range(num):
    xy.append(list(map(int, input().split())))

for a in range(num):
    for i in range(10):
        for j in range(10):
            whole[xy[a][0] + i][xy[a][1] + j] = 1

for i in range(100):
    for j in range(100):
        ar += whole[i][j]

print(ar)