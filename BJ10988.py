import sys

input = sys.stdin.readline

S = str(input())
T = 0
K = (len(S) - 1) // 2
for i in range(0, K):
    if S[i] == S[len(S) - i - 2]:
        T = T + 1

    else:
        continue

if T == K:
    print("1")

else:
    print("0")
