def find_max_profit_greedy_approach(matrix):
    max_profit_info = (0, 0, 0, 0)  # (stock_index, buy_day, sell_day, max_profit)

    # Iterate through each stock
    for stock_index, prices in enumerate(matrix):
        min_price = prices[0]
        max_profit = 0
        buy_day = 1
        sell_day = 1

        # Iterate through the days for each stock
        for current_day, price in enumerate(prices):
            # Check if current price is less than minimum price found so far
            if price < min_price:
                min_price = price
                buy_day = current_day + 1  # +1 to convert from 0-indexed to 1-indexed

            # Calculate profit if we sell on the current day
            current_profit = price - min_price

            # Check if current calculated profit is greater than the max profit so far
            if current_profit > max_profit:
                max_profit = current_profit
                sell_day = current_day + 1  # +1 to convert from 0-indexed to 1-indexed

        # Update the max_profit_info if the current stock's max profit is greater than the previous max profit
        if max_profit > max_profit_info[3]:
            max_profit_info = (stock_index + 1, buy_day, sell_day, max_profit)

    return max_profit_info

# Given input matrix A
A = [
    [12, 1, 5, 3, 16],
    [4, 4, 13, 4, 9],
    [6, 8, 6, 1, 2],
    [14, 3, 4, 8, 10]
]

# Find the stock with the maximum profit
result = find_max_profit_greedy_approach(A)

# Print the result
print(f"Stock to choose: {result[0]}, Buy on day: {result[1]}, Sell on day: {result[2]}, Max profit: {result[3]}")
print(f"The final output for the given matrix should be: [{result[0]}, {result[1]}, {result[2]}, {result[3]}]")


