import sys

input = sys.stdin.readline

S = str(input().rstrip())
A = []


for i in range(0, 26):
    A.append(-1)

for i in range(0, len(S)):
    if A[ord(S[i]) - 97] == -1:
        A[ord(S[i]) - 97] = i

    else:
        continue

for i in range(0, len(A)):
    print(A[i], end = " ")