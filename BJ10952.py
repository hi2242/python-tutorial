import sys

input = sys.stdin.readline

C = []
i = int(0)

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    i = i + 1
    C.append(A + B)

for j in range(0, i):
    print(C[j])
