import sys

input = sys.stdin.readline

N = int(input())
A = 1
B = 0
while True:
    if N <= A:
        B += 1
        break
    else:
        B += 1
        A += 6 * B
        continue

print(B)