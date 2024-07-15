import sys

input = sys.stdin.readline

S = str(input().strip())
count = 1

if len(S) == 0:
    count = 0

for i in range(0, len(S)):
    if S[i] == " " and len(S) != 1:
        count = count + 1

    else:
        continue

print(count)
