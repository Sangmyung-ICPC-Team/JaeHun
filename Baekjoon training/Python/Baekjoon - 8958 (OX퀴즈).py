t = int(input())

for i in range(1, t+1):
    string = input()
    sum = 0
    score = 0
    for j in string:
        if j == 'O':
            score += 1
        else:
            score = 0
        sum += score
    print(sum)
