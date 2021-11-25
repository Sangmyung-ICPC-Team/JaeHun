s = list(input())
k = input()

result = []
for i in s:
    if i.isdigit():
        continue
    else:
        result.append(i)

result = ''.join(result)

if k in result:
    print('1')
else:
    print('0')
