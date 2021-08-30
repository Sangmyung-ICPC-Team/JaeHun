import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0
sum = 0
result = 1000001
while True:
    if sum >= s:
        result = min(result, right - left)
        sum -= arr[left]
        left += 1
    elif right == n:
        break
    else:
        sum += arr[right]
        right += 1
    
if result == 1000001:
    result = 0
print(result)
