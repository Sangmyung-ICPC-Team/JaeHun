from collections import deque
#load deque
import sys
input = sys.stdin.readline

n = int(input())
adj_mat = []
max = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    adj_mat.append(list(map(int, input().split())))
    for j in range(n):
        if adj_mat[i][j] > max:
            max = adj_mat[i][j] # 최대 높이 구함

def bfs(x, y, visited, num):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                if adj_mat[nx][ny] > num and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

result = 0
for i in range(max): #비 x~max
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if adj_mat[j][k] > i and visited[j][k] == False: #비가 온 곳보다 높고 visited 아니면 탐색
                bfs(j, k, visited, i)
                cnt += 1
    if cnt > result:
        result = cnt
print(result)
