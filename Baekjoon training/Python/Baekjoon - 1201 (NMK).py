n, m, k = map(int, input().split())

if n < m+k-1 or n > m*k:
    print(-1)
else:
    cnt = [k]
    n -= k
    for _ in range(m-1):
        cnt.append(n // m-1)
    index = 1
    while sum(cnt[1:]) < n:
        if cnt[index] < k:
            cnt[index] += 1
        index += 1
        if index >= len(cnt):
            index = 1
    num = 0
    for i in range(len(cnt)):
        num += cnt[i]
        for j in range(num, num-cnt[i], -1):
            print(j, end = ' ')
