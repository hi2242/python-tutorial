X = int(input())
N = int(input())
C = []

for i in range(0, N):
    a, b = map(int, input().split())
    C.append(a * b)

if sum(C) == X:
    print("Yes")

else:
    print("No")