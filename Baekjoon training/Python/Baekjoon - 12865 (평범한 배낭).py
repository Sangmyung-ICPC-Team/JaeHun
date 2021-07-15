import sys
input = sys.stdin.readline
n, k = map(int, input().split())
bag = [[0, 0]]
for i in range(1, n+1):
    bag.append(list(map(int, input().split())))
arr = [[0] * (k + 1) for _ in range(n+1)] #2 dimension mtx
for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= bag[i][0]:
            arr[i][j] = max(arr[i-1][j], arr[i-1][j-bag[i][0]] + bag[i][1])
        else:
            arr[i][j] = arr[i-1][j]
print(arr[n][k])
