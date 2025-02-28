import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))

def solve(array, pick):
    temp = []

    for i in permutations(array, pick):
        temp.append(i)

    result = sorted(temp, key=lambda x : x)

    return result

answer = solve(arr, M)

for row in answer:
    print(' '.join(map(str, row)))