# [0] 기본 조건
# 창고 (10칸)
# 창고에는 로봇과 박스가 하나씩 있음
# 로봇에게 명령을 내려서 박스를 이동 (깃발까지)

# [1] 로봇에게 내릴 수 있는 명령
# 1. 인접한 빈칸으로 이동
# 2. 인접한 칸의 박스를 밀고 그 자리로 이동
def find():
    robot = box = flag = -1
    for i in range(len(command)):
        if command[i] == "@":
            robot = i

        elif command[i] == "#":
            box = i

        elif command[i] == "!":
            flag = i

    return robot, box, flag

# def move(i):
#     global command, count
#     status = -1

#     if command[i + 1] == ".":
#         command[i], command[i + 1] = command[i + 1], command[i]
#         count += 1
        
#     elif command[i + 1] == "#":
#         if command[i + 2] == "!":
#             count += 1
#             status = 1
#             return status
        
#         elif command[i + 2] == ".":
#             command[i + 1], command[i + 2] = command[i + 2], command[i + 1]
#             command[i], command[i + 1] = command[i + 1], command[i]
#             count += 1
            
#     return status

def solve():
    robot_index, box_index, flag_index = find()

    if robot_index < box_index < flag_index or flag_index < box_index < robot_index:
        print(abs(flag_index - robot_index) - 1)
        
    else:
        print(-1)

# 입력
# 창고의 상태
# 빈칸(.), 로봇(@), 박스(#), 깃발(!)
# @, #, !는 정확히 하나씩 주어짐
# 단, 박스가 처음부터 깃발에 있지 않음
command = list(input())
count = 0

# 출력
# 박스를 깃발로 옮기기 위한 명령 횟수 (못옮기는 경우는 -1 출력)
solve()