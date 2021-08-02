n, c = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()
start = 1
end = max(arr) - min(arr)

result = 0
while start <= end:
    total = 0
    cnt = 1
    mid = (start + end) // 2
    temp = min(arr)
    for i in range(1, len(arr)):
        if arr[i] >= mid + temp:
            cnt += 1
            temp = arr[i]
    if cnt < c:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)
