import sys

input = sys.stdin.readline

A = str(input())

print(len(A) - 1)

# sys.stdin.readline을 통해 개행문자가 포함되어 -1을 해주어야한다.
# int나 split은 개행문자를 지워준다.