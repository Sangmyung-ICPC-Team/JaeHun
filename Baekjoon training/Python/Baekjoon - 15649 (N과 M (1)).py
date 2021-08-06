import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

def solve():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
    for i in range(1, n+1):
        if i in arr:
            continue
        arr.append(i)
        solve()
        arr.pop()

solve()
