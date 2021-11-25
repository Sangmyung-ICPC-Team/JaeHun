import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

if __name__ == "__main__":
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]
    for _ in range(m):
        k, a, b = map(int, input().split())
        if k == 0:
            union(parent, a, b)
        elif k == 1:
            if find(parent, a) == find(parent, b):
                print('YES')
            else:
                print('NO')
