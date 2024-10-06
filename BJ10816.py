# 이진 탐색, 이분 탐색 설계
import sys

input = sys.stdin.readline

# 정수가 써있는 카드 묶음이 들어갈 l과 찾아야할 정수를 target을 파라미터로 받는다.
# 이분 탐색의 범위를 위한 start, end 또한 파라미터로 받는다.
def solve(l, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2
    if l[mid] == target:
        return count.get(target)
    elif l[mid] > target:
        # 중앙 값은 다시 탐색할 필요가 없기 때문에 mid-1으로 mid+1으로
        # 구간을 좁힌다.
        return solve(l, target, start, mid-1)
    else:
        return solve(l, target, mid+1, end)

N = int(input())
cardNum = sorted(list(map(int, input().split())))

M = int(input())
checkNumList = list(map(int, input().split()))

count = {}

# 카드에 써있는 정수를 key값으로 하는 value가 1인 딕셔너리를 생성하고
# 그 후부터는 카드에 해당하는 key값의 value를 1씩 증가시킨다.
for card in cardNum:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1
        
for checkNum in checkNumList:
    # result = count.get(checkNum, 0) # key가 없으면 0을 반환
    # print(result, end=" ")
    print(solve(cardNum, checkNum, 0, len(cardNum)-1), end=" ")

# # 딕셔너리란 key값과 value를 하나의 묶음으로 {key : value} 자료를
# # 저장하는 것이다.
# import sys

# input = sys.stdin.readline

# N = int(input())
# cardNum = list(map(int, input().split()))

# M = int(input())
# checkNumList = list(map(int, input().split()))

# # 딕셔너리 선언
# count = {}

# # 카드에 써있는 정수를 key값으로 하는 value가 1인 딕셔너리를 생성하고
# # 그 후부터는 카드에 해당하는 key값의 value를 1씩 증가시킨다.
# for card in cardNum:
#     if card in count:
#         count[card] += 1
#     else:
#         count[card] = 1

# # 체크해야하는 정수의 값을 key값으로 get하여 result에 저장한다.
# # 저장된 result의 값을 통해 원하는 출력물을 출력한다.
# for checkNum in checkNumList:
#     result = count.get(checkNum)
#     if result == None:
#         print(0, end = " ")
#     else:
#         print(result, end = " ")

# # Counter를 이용한 딕셔너리 추가
# import sys
# from collections import deque
# from collections import Counter

# input = sys.stdin.readline

# N = int(input())

# cardNum = list(map(int, input().split()))

# M = int(input())
# checkNumList = list(map(int, input().split()))

# # 딕셔너리를 이용하여 시간 복잡도를 낮추는 방법
# # Counter
# count = Counter(cardNum)

# result = []
# for checkNum in checkNumList:
#     result.append(count[checkNum])

# print(' '.join(map(str, result)))