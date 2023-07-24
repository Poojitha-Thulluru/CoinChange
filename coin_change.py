def get_coins_count(coins_array: list, amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins_array:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


try:
    coin_array = list(map(int, input("Enter coins separated by space : ").split()))
    target_amount = int(input("Enter the target amount : "))
    print("The number of coins required to get the total sum is : ", get_coins_count(coin_array, target_amount))
except ValueError:
    print("Invalid input. Enter only integers")
