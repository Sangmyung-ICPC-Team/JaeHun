s = int(input())
sum = 0
num = 1
cnt = 0
while(True):
    sum += num
    cnt += 1
    if(sum > s):
        cnt -= 1
        break
    num += 1
print(cnt)
