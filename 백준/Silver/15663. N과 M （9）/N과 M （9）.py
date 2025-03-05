import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))

def solve(array, pick):
    result = []
    for i in permutations(array, pick):
        result.append(i)

    temp = set(result)
    answer = sorted(temp, key = lambda x : x)
    return answer

for each in solve(arr, M):
    print(' '.join(map(str, each)))