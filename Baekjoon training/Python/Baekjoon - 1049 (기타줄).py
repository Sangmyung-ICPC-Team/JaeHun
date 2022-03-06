n, m = map(int, input().split())

min_p_cost = 1000
min_n_cost = 1000
for _ in range(m):
    package_cost, normal_cost = map(int, input().split())
    min_p_cost = min(min_p_cost, package_cost)
    min_n_cost = min(min_n_cost, normal_cost)

num = n // 6 + 1

print(min(min_p_cost * num, min_n_cost * n, (min_p_cost * (num-1) + (n - 6 * (num-1))*min_n_cost)))
