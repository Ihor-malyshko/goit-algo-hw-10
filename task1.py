def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    
    return result

if __name__ == "__main__":
    # тести
    test_cases = [123, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for amount in test_cases:
        result = find_coins_greedy(amount)
        print(f"Для суми {amount}: {result}")