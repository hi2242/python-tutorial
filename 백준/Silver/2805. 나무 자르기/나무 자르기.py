import sys

input = sys.stdin.readline

# 재귀 호출에서 반환을 제대로 하지 않으면 None이 반환된다.
# 시간복잡도와 공간복잡도를 고려했을 때 재귀보단 반복이 낫다.

def cutting(short, long):

    result = 0
    while short <= long:
        cutSum = 0
        cutLength = (short + long) // 2
        for i in range(tree):
            if treeLength[i] > cutLength:
                cutSum += treeLength[i] - cutLength

        if cutSum >= bring: # 나무를 모자라지 않게 가져가야한다.
            result = cutLength
            short = cutLength + 1

        else:
            long = cutLength - 1

    return result

tree, bring = map(int, input().split())

treeLength = list(map(int, input().split()))

# set에서는 인덱스로 접근할 수 없다.
result = cutting(0, max(treeLength))

print(result)