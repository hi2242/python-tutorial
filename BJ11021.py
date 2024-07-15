import sys
input = sys.stdin.readline

T = int(input())
C = []

for i in range(0, T):
    A, B = map(int, input().split())
    C.append(A + B)

for i in range(0, T):
    print("Case #%d: %d" %(i + 1, C[i]))