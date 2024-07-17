import sys

input = sys.stdin.readline

S = str(input().rstrip())
a = []
b = []
c = []
for i in range(65, 91):
    a.append(S.count(chr(i)))

for i in range(97, 123):
    b.append(S.count(chr(i)))

for i in range(0, len(a)):
    c.append(a[i] + b[i])

if c.count(max(c)) == 1:
    print(chr(c.index(max(c)) + 65))

else:
    print("?")