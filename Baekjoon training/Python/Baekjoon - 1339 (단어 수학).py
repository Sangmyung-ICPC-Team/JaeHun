n = int(input())
word = []
for _ in range(n):
    word.append(input())

alphabet = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 
'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 
'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}

for a in word:
    for i in range(len(a)):
        num = 10 ** (len(a)-i-1)
        alphabet[a[i]] += num

alpha_list = []
for i in alphabet.values():
    if i > 0:
        alpha_list.append(i)

answer = 0
sorted_list = sorted(alpha_list, reverse=True)
for i in range(len(sorted_list)):
    answer +=  sorted_list[i] * (9 -i)

print(answer)
