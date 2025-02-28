import sys

input = sys.stdin.readline

# N = int(input())

# A = list(map(int, input().split()))

# 시간초과 (복잡도 O(N^3))

# def solve(lengthArr, array):
#     lengthTemp = 0
#     countTemp = 0

#     while(countTemp != lengthArr):
#         for j in range(countTemp + 1,  lengthArr):
#             temp = [array[countTemp]]
#             for i in array[j:]:
#                 if temp[len(temp) - 1] < i:
#                     temp.append(i)

#             if lengthTemp < len(temp):
#                 lengthTemp = len(temp)

#         countTemp += 1

#     return lengthTemp

# print(solve(N, A))

# DP를 이용한 풀이이다.
# 리스트의 각 요소가 끝이라고 생각했을 때 linked list처럼 더 작은 수를 이어 붙이는 형태

n = int(input())
arr = list(map(int, input().split()))

d = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))