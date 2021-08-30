n = int(input())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = n-1

exist = arr[left] + arr[right]
ex_left = left
ex_right = right

while left < right:
    temp = arr[left] + arr[right]
    if abs(temp) < abs(exist):
        exist = temp
        ex_left = left
        ex_right = right
        if exist == 0:
            break
    if temp < 0:
        left += 1
    elif temp > 0:
        right -= 1

print(arr[ex_left], arr[ex_right])
