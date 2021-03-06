n = int(input())

arr = [2, 5]

dp = [100001] * (n + 1)

dp[0] = 0
for i in range(2):
    for j in range(arr[i], n+1):
        if dp[j - arr[i]] != 100001:
            dp[j] = min(dp[j], dp[j-arr[i]] + 1)

if dp[n] == 100001:
    print(-1)
else:
    print(dp[n])
