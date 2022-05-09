INF = int(1e9)

n, m = map(int, input().split())
start_point = int(input())

graph = [[]for i in range(n+1)]
visited = [False for i in range(n+1)]
distance = [INF for i in range(n+1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

def get_smallest_node():
    min = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min and not visited[i]:
            min = distance[i]
            index = i
    return index

def dijkstra(start):
    visited[start] = True
    distance[start] = 0
    for i in graph[start]:
        if i[1] < distance[i[0]]:
            distance[i[0]] = i[1]
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            weight = distance[now] + j[1]
            if weight < distance[j[0]]:
                distance[j[0]] = weight
dijkstra(start_point)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])