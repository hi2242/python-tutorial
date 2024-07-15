import sys

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
B = []
avg = 0

for i in range(0, N):
    B.append(float(A[i] / max(A)) * 100)

for i in range(0, N):
    avg = avg + B[i]

print(avg / N)