import math # for fac

c = int(input())
result = False
for _ in range(c):
    arr = input().split()
    arr[1] = int(arr[1]) #max
    arr[2] = int(arr[2]) #case
    arr[3] = int(arr[3]) #limit
    if arr[0][2] == 'N':
        if arr[0][3] =='^':
            if arr[0][4] == '2':
                if arr[3] * 10**8 >= arr[1] ** 2 * arr[2]:
                    result = True
                else:
                    result = False
            else:
                if arr[3] * 10**8 >= arr[1] ** 3 * arr[2]:
                    result = True
                else:
                    result = False
        elif arr[0][3] == ')':
            if arr[3] * 10**8 >= arr[1] * arr[2]:
                result = True
        elif arr[0][3] == '!':
            if arr[3] * 10**8 >= math.factorial(arr[1]) * arr[2]:
                result = True
            else:
                result = False
    else:
        if arr[3] * 10**8 >= 2 ** arr[1] * arr[2]:
            result = True
        else:
            result = False
    
    if result == True:
        print('May Pass.')
    else:
        print('TLE!')
