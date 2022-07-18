from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    visited[x][y] = True
    now = graph[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and graph[nx][ny] == now:
            dfs(nx, ny)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))
visited = [[False] for _ in range(n)]

rgb = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            rgb += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

rg_blind = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            rg_blind += 1

print(rgb, rg_blind)