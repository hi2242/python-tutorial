import sys

input = sys.stdin.readline

N, B = input().split()
N = list(map(str, N.rstrip()))
B = int(B)

C = []
result = 0

for i in range(len(N)):
    if 65 <= ord(N[i]) <= 90:
        C.append(ord(N[i]) - 55)
    
    elif 48 <= ord(N[i]) <= 57:
        C.append(int(N[i]))
    
    else:
        continue

for i in range(len(N)):
    result += C[len(N) - 1 - i] * (B ** i)

print(result)

# import sys

# input = sys.stdin.readline

# N, B = input().split()
# N = list(map(str, N.rstrip()))
# B = int(B)

# C = []
# result = 0

# for i in range(len(N)):
#     if 65 <= ord(N[i]) <= 90:
#         C.append(ord(N[i]) - 55)

# for i in range(len(N)):
#     if 65 <= ord(N[len(N) - 1 - i]) <= 90:
#         result += (ord(N[len(N) - 1 - i]) - 55) * (B ** i)
    
#     elif 48 <= ord(N[len(N) - 1 - i]) <= 57:
#         result += int(N[len(N) - 1 - i]) * (B ** i)

#     else:
#         continue

# print(result)