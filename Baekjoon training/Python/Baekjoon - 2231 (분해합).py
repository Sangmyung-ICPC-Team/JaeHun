N = int(input())
result = 0
for i in range(1, N+1):
    num = list(map(int, str(i)))
    s_of_num = i + sum(num)
    if(s_of_num == N):
        result = i
        break
print(result)
