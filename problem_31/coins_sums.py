def count_coin_combinations(target, coins):

    # Initialize a DP array where dp[i] represents the number of ways to make amount i
    dp = [0] * (target + 1)
    dp[0] = 1  # Base case: 1 way to make 0p (using no coins)
    
    for coin in coins:
        for amount in range(coin, target + 1):
            dp[amount] += dp[amount - coin]
    
    return dp[target]

# Define the coin denominations and target amount
coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200

# Expected answoer: 73682
print(count_coin_combinations(target, coins))