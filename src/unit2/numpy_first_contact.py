import numpy as np

prices = np.array([3, 5, 8, 10, 12, 16, 17, 20])

print(prices.mean())
print(prices.max())
print(prices.min())

print(f'Median {np.median(prices)}')

vat = 1.19

final_prices = prices * vat
print(final_prices)