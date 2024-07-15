import sys
input = sys.stdin.readline

T = int(input())
C = []
D = []

for i in range(0, T):
    A, B = map(int, input().split())
    C.append(A)
    D.append(B)

for i in range(0, T):
    print("Case #%d: %d + %d = %d" %(i + 1, C[i], D[i], C[i] + D[i]))