n = int(input())
crane = list(map(int, input().split()))
m = int(input())
product = list(map(int, input().split()))

cnt = 0
crane = sorted(crane, reverse=True)
product = sorted(product, reverse=True)


if(crane[0] < product[0]):
    print(-1)
else:
    while len(product) > 0:
        for i in crane:
            for j in range(len(product)):
                if i >= product[j]:
                    product.remove(product[j])
                    break
        cnt += 1
    print(cnt)
