from collections import deque

def bfs(graph, start):
    cnt = 1
    queue = deque([start])
    visited[start] = True
    result[start] = cnt
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                cnt += 1
                queue.append(i)
                visited[i] = True
                result[i] = cnt
                
n, m, r = map(int, input().split())
visited = [False for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
result = [0 for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n+1):
    graph[i].sort()

bfs(graph, r)
for i in result[1:]:
    print(i)