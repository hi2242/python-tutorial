import sys

input = sys.stdin.readline

S = str(input().rstrip())
C = 0

for i in range (0, len(S)):
    if i != len(S) - 1 and S[i] == "c" and S[i + 1] == "=":
        continue
    elif i != len(S) - 1 and S[i] == "c" and S[i + 1] == "-":
        continue
    elif i != len(S) - 1 and i != len(S) - 2 and S[i] == "d" and S[i + 1] == "z" and S[i + 2] == "=":
        C = C - 1

    elif i != len(S) - 1 and S[i] == "d" and S[i + 1] == "-":
        continue
    elif i != len(S) - 1 and S[i] == "l" and S[i + 1] == "j":
        continue
    elif i != len(S) - 1 and S[i] == "n" and S[i + 1] == "j":
        continue
    elif i != len(S) - 1 and S[i] == "s" and S[i + 1] == "=":
        continue
    elif i != len(S) - 1 and S[i - 1] != "d" and S[i] == "z" and S[i + 1] == "=":
        continue
    else:
        C = C + 1

print(C)