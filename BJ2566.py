import sys

input = sys.stdin.readline

row = []

for i in range(9):
    row.append(list(map(int, input().split())))

big = [max(row[i][j] for j in range(9) for i in range(9))]

print(max(big))

for i in range(9):
    for j in range(9):
        if row[i][j] == max(big):
            print(i + 1, j + 1)
