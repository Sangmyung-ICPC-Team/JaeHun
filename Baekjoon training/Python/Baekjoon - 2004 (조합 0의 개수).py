n, m = map(int, input().split())

def cnt_num(n, var):
    cnt = 0
    while n:
        n //= var
        cnt += n
    return cnt

# 2x5 = 10 (min(2, 5)이 곧 끝자리 0의 개수)
five_cnt = cnt_num(n, 5) - cnt_num(m, 5) - cnt_num(n-m, 5)
two_cnt = cnt_num(n, 2) - cnt_num(m, 2) - cnt_num(n-m, 2)

result = min(five_cnt, two_cnt)
print(result)
