import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

start = 0
end = k

result = 9
while start <= end:
    total = 0
    mid = (start + end) // 2

    for i in range(1, n+1):
        total += min(mid//i, n)
    
    if total < k:
        start = mid + 1
    else:
        result = mid
        end = mid - 1
print(result)
