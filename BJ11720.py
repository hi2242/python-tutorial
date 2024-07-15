import sys

input = sys.stdin.readline

N = int(input())
A = str(input().rstrip())
B = 0

for i in range(0, N):
    B = B + int(A[i])
    
print(B)