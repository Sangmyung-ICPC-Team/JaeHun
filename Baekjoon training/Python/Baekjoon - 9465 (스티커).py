t = int(input())
for _ in range(t):
    arr = []
    n = int(input())
    for _ in range(2):
        arr.append(list(map(int, input().split())))
    for i in range(1, n):
        #자기 옆면은 x 최대값 or 그 왼쪽 수 중 최대 수와 오른쪽 아래 (자신) 을 더함
        if i == 1:
            arr[0][i] += arr[1][i-1]
            arr[1][i] += arr[0][i-1]
        else:
            arr[0][i] += max(arr[1][i-1], arr[1][i-2])
            arr[1][i] += max(arr[0][i-1], arr[0][i-2])
    print(max(arr[0][n-1], arr[1][n-1]))