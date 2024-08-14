import sys

input = sys.stdin.readline

N, M = map(int, input().split())

A = list(map(int, input().split()))
B = M

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if 0 <= M - (A[i] + A[j] + A[k]) < B:
                B = M - (A[i] + A[j] + A[k])
            
            else:
                continue

print(M - B)