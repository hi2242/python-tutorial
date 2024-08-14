import sys

input = sys.stdin.readline

word = []
num = []

# for i in range(5):
#     word.append(list(map(str, input().split())))

# for i in range(5):
#     num.append(len(word[i][0]))

# for i in range(15):
#     for j in range(5):
#         if num[j] - 1 < i:
#             continue
#         else:
#             print(word[j][0][i], end="")

for i in range(5):
    word.append(list(map(str, input().rstrip())))

for i in range(5):
    num.append(len(word[i]))

for i in range(15):
    for j in range(5):
        if num[j] - 1 < i:
            continue
        else:
            print(word[j][i], end="")