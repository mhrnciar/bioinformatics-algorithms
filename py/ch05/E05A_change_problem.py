# Change Problem:
# Find the minimum number of coins needed to make change
#   Input: An integer money and an array COINS of d positive integers
#   Output: The minimum number of coins with denominations COINS that changes money


def DPChange(money, coins):
    min_num_coins = [0]

    for m in range(1, money + 1):
        min_num_coins.append(9999)

        for coin in coins:
            if m >= coin:
                if min_num_coins[m-coin] + 1 < min_num_coins[m]:
                    min_num_coins[m] = min_num_coins[m-coin] + 1

    return min_num_coins[money]


if __name__ == "__main__":
    _money = int(input("Money: "))
    _coins = [int(x) for x in input("Coins: ").split(',')]

    print(DPChange(_money, _coins))
