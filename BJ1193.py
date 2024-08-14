import sys

input = sys.stdin.readline

X = int(input())

N = 1

while True:
    if X > N:
        X -= N
        N += 1
        continue
    else:
        break

if N % 2 == 0:
    print(X, N - X + 1, sep="/")

else:
    print(N - X + 1, X, sep="/")