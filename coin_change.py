
n, m = map(int, input().split())
coins = list(map(int, input().rstrip().split()))

memo = [0] * (n + 1)
memo[0] = 1

for coin in coins:
    for change in range(coin, n + 1):
        memo[change] += memo[change - coin]

print(memo[n])
