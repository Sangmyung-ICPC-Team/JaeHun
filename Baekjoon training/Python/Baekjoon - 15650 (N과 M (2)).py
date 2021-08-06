n, m = map(int, input().split())
arr = []

def solve(start):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(start, n+1):
        if i in arr:
            continue
        arr.append(i)
        solve(i+1)
        arr.pop()

solve(1)
