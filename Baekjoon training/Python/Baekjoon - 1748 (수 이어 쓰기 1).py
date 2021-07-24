n = int(input())
arr = [int('9' + '0' * i)for i in range(0, len(str(n)))]
result = 0
for i, j in enumerate(arr):
    if j == arr[-1]:
        result += len(str(j)) * (n - sum(arr[:-1]))
    else:
        i += 1
        result += i * j
print(result)
