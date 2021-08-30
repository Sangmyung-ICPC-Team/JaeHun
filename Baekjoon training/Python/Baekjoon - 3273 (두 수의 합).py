import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
x = int(input())

cnt = 0
left = 0
right = n-1

while left != right:
    if arr[left] + arr[right] == x:
        cnt += 1
        left += 1
    elif arr[left] + arr[right] > x:
        right -= 1
    else:
        left += 1
print(cnt)
