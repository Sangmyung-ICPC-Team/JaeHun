a, b = input().split()
bet_len = len(b) - len(a)
if bet_len == 0:
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    print(cnt)
else:
    result = []
    for i in range(bet_len + 1):
        cnt = 0
        for j in range(len(a)):
            if a[j] != b[i+j]:
                cnt += 1
        result.append(cnt)
    print(min(result))