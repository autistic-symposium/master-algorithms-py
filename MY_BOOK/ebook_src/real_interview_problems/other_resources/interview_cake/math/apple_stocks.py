#!/bin/python

"""
Grab Apple's stock prices and put them in a list called stock_prices, where:

The indices are the time (in minutes) past trade opening time, which was 9:30am local time.
The values are the price (in US dollars) of one share of Apple stock at that time.
So if the stock cost $500 at 10:30am, that means stock_prices[60] = 500.

Write an efficient function that takes stock_prices and returns the best profit I could have made from one purchase and one sale of one share.
"""

def apple_stock_profit(stock_prices):

    min_s, max_s = max(stock_prices), 0

    while stock_prices:
        stock = stock_prices.pop()
        min_s = min(min_s, stock)
        max_s = max(max_s, stock)

    return max_s - min_s


stock_prices = [10, 7, 5, 8, 11, 9]
print apple_stock_profit(stock_prices)
print("Should return 6 (buying for $5 and selling for $11)")