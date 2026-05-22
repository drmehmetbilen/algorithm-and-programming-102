def greedy_coin_change(amount, coins):
    """
    Return a greedy coin choice for the given amount.
    Coins are chosen from largest to smallest.
    """
    remaining = amount
    chosen = []

    for coin in sorted(coins, reverse=True):
        while remaining >= coin:
            chosen.append(coin)
            remaining -= coin

    return chosen, remaining


if __name__ == "__main__":
    canonical_coins = [25, 10, 5, 1]
    canonical_amount = 63
    chosen, remaining = greedy_coin_change(canonical_amount, canonical_coins)

    print("Canonical system example")
    print("Coins:    ", canonical_coins)
    print("Amount:   ", canonical_amount)
    print("Greedy:   ", chosen)
    print("Remaining:", remaining)

    tricky_coins = [4, 3, 1]
    tricky_amount = 6
    chosen, remaining = greedy_coin_change(tricky_amount, tricky_coins)

    print("\nCounterexample")
    print("Coins:    ", tricky_coins)
    print("Amount:   ", tricky_amount)
    print("Greedy:   ", chosen)
    print("Remaining:", remaining)
    print("Better:   ", [3, 3], "uses fewer coins than", chosen)
