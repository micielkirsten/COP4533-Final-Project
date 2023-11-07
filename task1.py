def find_max_profit_brute_force(matrix):
    max_profit_info = (0, 0, 0, 0)  # (stock_index, buy_day, sell_day, max_profit)

    # Iterate through each stock
    for stock_index, prices in enumerate(matrix):
        # Initialize max_profit for this stock
        max_profit = 0
        buy_day = 0
        sell_day = 0

        # Iterate through each day to buy
        for i in range(len(prices)):
            # Iterate through each day to sell
            for j in range(i+1, len(prices)):
                # Calculate the profit
                current_profit = prices[j] - prices[i]
                # Update max_profit if the current_profit is greater
                if current_profit > max_profit:
                    max_profit = current_profit
                    buy_day = i + 1  # +1 to convert from 0-indexed to 1-indexed
                    sell_day = j + 1  # +1 to convert from 0-indexed to 1-indexed

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

# Find the stock with the maximum profit using the brute force approach
result = find_max_profit_brute_force(A)

# Print the result
print(f"Stock to choose: {result[0]}, Buy on day: {result[1]}, Sell on day: {result[2]}, Max profit: {result[3]}")
print(f"The final output for the given matrix should be: [{result[0]}, {result[1]}, {result[2]}, {result[3]}]")
