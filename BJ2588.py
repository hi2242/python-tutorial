import math

A = int(input())
B = int(input())

for i in range(1, 4):
    print(A * (int(B / math.pow(10, i - 1)) - (int(B / math.pow(10, i)) * 10)))

print(A * B)