t = int(input())

cnt = 0
for i in range(t):
    flag = 1
    arr = input()
    for j in range(len(arr)):
        for k in range(0, j):
            if arr[j-1] != arr[j] and arr[j] == arr[k]:
                flag = 0
                break
    if flag == 1:
        cnt += 1
print(cnt)   
