import sys
input = sys.stdin.readline

n, m = map(int, input().split())

floor = []
for _ in range(n):
    floor.append(list(input()))

cnt = 0
for i in range(n):
    temp = "."
    for j in range(m):
        if floor[i][j] == "-":
            if floor[i][j] != temp:
                cnt += 1
        temp = floor[i][j]

for i in range(m):
    temp = "."
    for j in range(n):
        if floor[j][i] == "|":
            if floor[j][i] != temp:
                cnt += 1
        temp = floor[j][i]

print(cnt)
