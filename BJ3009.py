import sys

input = sys.stdin.readline
x = []
y = []

for _ in range(3):
    a, b = map(int,input().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()

if x[0] == x[1]:
    a = x[2]

else:
    a = x[0]

if y[0] == y[1]:
    b = y[2]

else:
    b = y[0]

print(a, b)