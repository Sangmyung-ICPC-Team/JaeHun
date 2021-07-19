import sys
input = sys.stdin.readline
n = int(input())
arr = [0, 1, 2] + [0] * n
for i in range(3, n+1):
    arr[i] = arr[i-1] + arr[i-2]
print(arr[n] % 10007)
