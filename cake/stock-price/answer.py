

def get_max_profit(stock_prices):

    known_lowest = stock_prices[0]
    known_highest = stock_prices[1]
    # Only profit we can possibly make right now.
    max_profit = known_highest - known_lowest

    for current_price in stock_prices[2:]:
        # Is the current price higher than earlier in the day?
        known_highest = max(current_price, known_highest)

        # Try selling.
        max_profit = known_highest - known_lowest

        # Is the current price lower than earlier in the day?
        known_lowest = min(current_price, known_lowest)

    print(known_lowest, known_highest)
    return max_profit


if __name__ == "__main__":
    stock_prices = [10, 7, 5, 8, 11, 9]

    print(get_max_profit(stock_prices))
    # Returns 6 (buying for $5 and selling for $11)
