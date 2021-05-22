from collections import deque
#load deque

def bfs(vertex):
    visited[vertex] = 1
    queue = deque()
    queue.append(vertex)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for i in range(1, N+1, 1):
            if adj_mat[vertex][i] == 1 and visited[i] == 0:
                visited[i] = 1
                queue.append(i)

def dfs(vertex):
    print(vertex, end=' ')
    visited[vertex] = 1
    for i in range(1, N+1, 1):
        if adj_mat[vertex][i] == 1 and visited[i] == 0:
            dfs(i)

N, M, vertex = map(int, input().split())
    #map: 여러개 입력 시 사용
    #split(): 공백
adj_mat = [[0] * (N+1) for i in range(N+1)]
visited = [0 for i in range(N+1)]
for i in range(M):
    edge_x, edge_y = map(int, input().split())
    adj_mat[edge_x][edge_y] = 1
    adj_mat[edge_y][edge_x] = 1


dfs(vertex)
print()
visited = [0 for i in range(N+1)]
bfs(vertex)
