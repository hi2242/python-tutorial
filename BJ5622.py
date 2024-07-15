import sys

input = sys.stdin.readline

S = str(input())
A = []
T = 0

for i in range(0, len(S)):
    if ord(S[i]) >= 65 and ord(S[i]) <= 67:
        A.append(2)

    elif ord(S[i]) >= 68 and ord(S[i]) <= 70:
        A.append(3)

    elif ord(S[i]) >= 71 and ord(S[i]) <= 73:
        A.append(4)

    elif ord(S[i]) >= 74 and ord(S[i]) <= 76:
        A.append(5)

    elif ord(S[i]) >= 77 and ord(S[i]) <= 79:
        A.append(6)

    elif ord(S[i]) >= 80 and ord(S[i]) <= 83:
        A.append(7)

    elif ord(S[i]) >= 84 and ord(S[i]) <= 86:
        A.append(8)

    elif ord(S[i]) >= 87 and ord(S[i]) <= 90:
        A.append(9)

    else:
        continue

for i in range(0, len(A)):
    T = T + A[i]

print(T + len(A))