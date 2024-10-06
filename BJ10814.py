import sys

input = sys.stdin.readline

N = int(input())
clientList = []

for _ in range(N):
    client = list(input().split())
    clientList.append(client)

# string 타입으로 저장된 숫자는 11이 9보다 먼저인 점을 유의할 것
for row in sorted(clientList, key = lambda x : int(x[0])):
    print(" ".join(map(str, row)))