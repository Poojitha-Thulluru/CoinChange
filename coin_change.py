def get_coins_count(coins: list, amount: int) -> int:
    memo: dict = {}

    def min_coins_needed(amount):
        if amount < 0:
            return -1

        if amount == 0:
            return 0

        if amount in memo:
            return memo[amount]

        min_coins = float('inf')
        for coin in coins:
            remaining_coins = min_coins_needed(amount - coin)
            if remaining_coins >= 0:
                min_coins = min(min_coins, remaining_coins + 1)

        memo[amount] = min_coins if min_coins != float('inf') else -1
        return memo[amount]

    return min_coins_needed(amount)


try:
    coin_array = list(map(int, input("Enter coins separated by space : ").split()))
    target_amount = int(input("Enter the target amount : "))
    print("The number of coins required to get the total sum is : ", get_coins_count(coin_array, target_amount))
except ValueError:
    print("Invalid input. Enter only integers")
