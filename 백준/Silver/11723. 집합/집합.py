import sys

input = sys.stdin.readline
# set은 append등을 사용할 수 없으므로 append는 add로 사용하는 등의
# 변경이 필요하다.
# add, discard는 이미 set 내에 값이 존재하는지 확인 후 추가/삭제한다.
# discard = 존재여부 확인 + remove 기능
# range(1, 21)만 해도 1 ~ 20까지의 수를 의미한다.
# 새로운 객체를 할당하는 방식보다 copy나 clear를 통해서 빠르고 효율적으로
# 작동시킨다.
S = set()
fullS = set(map(str, range(1, 21)))

M = int(input())
for _ in range(M):
    command = list(input().split())
    if command[0] == "add":
        S.add(command[1])
    elif command[0] == "remove":
        S.discard(command[1])
    elif command[0] == "check":
        if command[1] in S:
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        if command[1] in S:
            S.remove(command[1])
        else:
            S.add(command[1])
    elif command[0] == "all":
        S = fullS.copy()
    elif command[0] == "empty":
        S.clear()