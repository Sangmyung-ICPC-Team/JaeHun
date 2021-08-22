import sys
sys.setrecursionlimit(100000000)

t = int(input())
result = []

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 2

        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1
    
    cnt = 0

    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                cnt += 1
    
    result.append(cnt)

for i in result:
    print(i)
