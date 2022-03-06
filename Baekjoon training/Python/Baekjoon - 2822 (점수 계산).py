arr = []
for _ in range(8):
    arr.append(int(input()))

sum = 0
result = []
for _ in range(5):
    sum += max(arr)
    idx = arr.index(max(arr))
    result.append(idx+1)
    arr[idx] = 0

print(sum)
print(*(sorted(result)))
