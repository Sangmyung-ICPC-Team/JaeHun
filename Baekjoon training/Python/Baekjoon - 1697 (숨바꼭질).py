from collections import deque

def bfs(graph, start):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        if v == k:
            print(graph[v])
            break
        for i in (v+1, v-1, 2*v):
            if 0 <= i <= 100000 and not graph[i]:
                graph[i] = graph[v] + 1
                queue.append(i)
    
n, k = map(int, input().split())
graph = [0 for i in range(100001)]
bfs(graph, n)