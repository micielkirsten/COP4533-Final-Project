def find_max_profit_dp(prices):
    if not prices:
        return 0, 0, 0

    n = len(prices)
    if n < 2:
        return 0, 0, 0

    # Arrays to store the maximum profit and last buy/sell days
    dp = [0] * n  # dp[i] will store the maximum profit up until day i
    buy_day = [0] * n
    sell_day = [0] * n

    # Initializing the first day's values
    dp[0] = 0
    min_price = prices[0]
    min_price_day = 0

    for i in range(1, n):
        if prices[i] < min_price:
            min_price = prices[i]
            min_price_day = i

        # Calculate profit if we sell on day i
        profit = prices[i] - min_price
        if profit > dp[i-1]:
            dp[i] = profit
            buy_day[i] = min_price_day
            sell_day[i] = i
        else:
            dp[i] = dp[i-1]
            buy_day[i] = buy_day[i-1]
            sell_day[i] = sell_day[i-1]

    # The last element in dp will contain the maximum profit
    return dp[-1], buy_day[-1] + 1, sell_day[-1] + 1

# Given input matrix A
A = [
    [7, 1, 5, 3, 9],
    [2, 4, 3, 7, 9],
    [5, 8, 9, 1, 2],
    [9, 3, 14, 8, 7]
]

# Find the stock with the maximum profit and corresponding days
max_profit_info = (0, 0, 0, 0)
for index, prices in enumerate(A):
    max_profit, buy_day, sell_day = find_max_profit_dp(prices)
    if max_profit > max_profit_info[3]:
        max_profit_info = (index + 1, buy_day, sell_day, max_profit)

# Print the result
print(f"Stock to choose: {max_profit_info[0]}, Buy on day: {max_profit_info[1]}, Sell on day: {max_profit_info[2]}, Max profit: {max_profit_info[3]}")
print(f"The final output for the given matrix should be: [{max_profit_info[0]}, {max_profit_info[1]}, {max_profit_info[2]}, {max_profit_info[3]}]")
