arr = str(input())
result = []

for _ in arr:
    result.append(arr)
    arr = arr[1:]

for i in sorted(result):
    print(i)
