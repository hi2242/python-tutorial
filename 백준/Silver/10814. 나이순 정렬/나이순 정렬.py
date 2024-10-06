import sys

input = sys.stdin.readline

N = int(input())
clientList = []

for _ in range(N):
    client = list(input().split())
    clientList.append(client)

for row in sorted(clientList, key = lambda x : int(x[0])):
    print(" ".join(map(str, row)))