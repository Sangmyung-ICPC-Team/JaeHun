def LIS_binary(arr):
    for i in arr:
        if result[-1] < i:
            result.append(i)
        else:
            low = 0
            high = len(result) - 1

            while low < high:
                mid = (low + high) // 2
                if result[mid] < i:
                    low = mid + 1
                else:
                    high = mid
            result[high] = i
                
n = int(input())
a = list(map(int, input().split()))
result = [0]
LIS_binary(a)
print(len(result)-1)