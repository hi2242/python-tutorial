import sys

input = sys.stdin.readline

N = int(input())
# set을 이용하면 리스트 내에 중복도 제거 할 수 있고 해시 테이블이라는
# 자료구조를 기반으로 동작하기 때문에 원소를 찾을 때 O(1)만큼만 시간이 걸린다.
# 최악의 경우는 시간 복잡도가 O(N)이 될 수도 있다.
rowA = set(map(int, input().split()))

M = int(input())

rowM = list(map(int, input().split()))

for i in range(M):
    if rowM[i] in rowA:
        print("1")

    else:
        print("0")
