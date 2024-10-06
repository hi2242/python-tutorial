# 파이썬에서는 stack 구조가 없기 때문에 list를 통해서 구현한다.
import sys

input = sys.stdin.readline

N = int(input())

commandList = []

for _ in range(N):
    command = list(input().split())
    if command[0] == "push":
        commandList.append(command[1])
    elif command[0] == "pop":
        if len(commandList) != 0:
            print(commandList.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(commandList))
    elif command[0] == "empty":
        if len(commandList) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "top":
        if len(commandList) != 0 and commandList[len(commandList) - 1] != None:
            print(commandList[len(commandList) - 1])
        else:
            print(-1)
    else:
        continue