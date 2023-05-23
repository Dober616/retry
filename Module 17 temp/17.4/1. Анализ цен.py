original_prices = [-12, 3, 5, -2, 1]
new_prices = [i if i > 0 else 0 for i in original_prices]
print(new_prices)
print("Мы потеряли: ",  sum(original_prices) - sum(new_prices))
