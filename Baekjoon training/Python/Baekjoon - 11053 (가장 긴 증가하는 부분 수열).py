import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
arr = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and arr[i] < arr[j]:
            arr[i] = arr[j]
    arr[i] += 1
print(max(arr))
