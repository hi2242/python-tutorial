import sys

input = sys.stdin.readline

T = int(input())
P = []
H = []
K = [0]


for i in range(0, T):
    R, S = input().split()
    R = int(R)
    S = str(S).rstrip()
 
    K.append(R * len(S))
    for j in range(0, len(S)):
        for v in range(0, R):
            P.append(S[j])

for i in range(0, T):
    for j in range(sum(K[0:i+1]) ,sum(K[0:i+2])):
        print(P[j], end = "")
    if i < T - 1:
        print(end = "\n")