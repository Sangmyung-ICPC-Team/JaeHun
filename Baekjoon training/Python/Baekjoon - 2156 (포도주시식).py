n = int(input())
wine = [0]
for i in range(n):
    wine.append(int(input()))
arr = [0]
arr.append(wine[1])
if n > 1:
    arr.append(wine[1] + wine[2])
for i in range(3, n+1):
    arr.append(max(arr[i-1], arr[i-3] + wine[i-1] + wine[i], arr[i-2] + wine[i]))
print(arr[n])
