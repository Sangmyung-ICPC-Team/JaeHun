n = int(input())
word = []
for _ in range(n):
    word.append(input())     
 
setting = list(set(word))
 
sorting= []
 
for i in setting:
    sorting.append((len(i), i)) 
 
sorting.sort()                  
 
for len, i in sorting:     
    print(i)
