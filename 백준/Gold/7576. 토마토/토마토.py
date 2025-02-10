# 1. 대입 연산자로 할당을 하면 객체에 대한 참조만 하게 된다. (연동된다.)
# 2. copy를 통해 얕은 복사를 하면 원본 객체와 복사본 객체가 동일한 객체를 참조하게 되는데
# 참조하는 객체에 변동이 없다면 서로 간 간섭은 없다.
# 3. deepcopy를 이용하면 원본 객체아 복사본 객체가 완전한 독립이 된다.

# 예외처리 방법
# 1. try : 예외 검사 구문
# 2. except : 해당 에러가 발생하면 실행할 구문
# 3. else : 예외가 없으면 실행할 구문
# 4. finally : 예외와 관계없이 실행할 구문

# index함수를 이용하여 존재 여부를 체크할 때 존재하면 인덱스를 반환하고
# 존재하지 않는다면 ValueError를 반환한다.
# index함수는 여러 개가 존재할 때 처음 찾는 것에 대해서만 인덱스를 반환한다.

import sys
from collections import deque

input = sys.stdin.readline

row, column = map(int, input().split())

grid = []

visited = [[0] * row for _ in range(column)]

for _ in range(column):
    grid.append(list(map(int, input().split())))

moveX = [-1, 1, 0, 0]
moveY = [0, 0, -1, 1]

def solve():
    d = deque()
    d2 = deque()

    rowCount = 0

    for y in range(column):
        for x in range(row):
            if grid[y][x] == 1:
                d2.append((y, x))
                visited[y][x] = 1
    # for eachRow in grid:
    #     try:
    #         findIndex = eachRow.index(1)
    #         d2.append((rowCount, findIndex))
    #         visited[rowCount][findIndex] = 1
            

    #     except ValueError:
    #         pass

    #     rowCount += 1

    dayCount = -1

    while d2:
        dayCount += 1
        d = d2.copy()
        d2.clear()

        while d:
            dy, dx = d.popleft()
            
            for i in range(4):
                newX = moveX[i] + dx
                newY = moveY[i] + dy

                if 0 <= newX < row and 0 <= newY < column and visited[newY][newX] == 0 and grid[newY][newX] == 0:
                    d2.append((newY, newX))
                    grid[newY][newX] = 1
                    visited[newY][newX] = 1 

    return dayCount

result = solve()

for eachRow in grid:
    if 0 in eachRow:
        print(-1)
        break
else:
    print(result)