import sys

input = sys.stdin.readline
# 해시 함수
L = int(input())

st = list(map(str, input().rstrip()))

result = 0
M = 1234567891

for i in range(L):
    result += (ord(st[i]) - 96) * (31 ** i)

print(result % M)