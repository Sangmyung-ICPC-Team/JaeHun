c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alphabet = input()
for i in c:
    alphabet = alphabet.replace(i, '*')
print(len(alphabet))
