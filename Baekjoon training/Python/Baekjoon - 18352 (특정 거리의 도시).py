from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[]for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

distance = [-1] * (n+1)

def bfs(graph, start, distance):
    queue = deque([start])
    distance[start] = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if distance[i] == -1:
                queue.append(i)
                distance[i] = distance[v] + 1

bfs(graph, x, distance)

for i in range(n+1):
    if distance[i] == k:
        print(i)
if k not in distance:
    print(-1)
