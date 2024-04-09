prices = [10, 20, 30]
total = 0
for i in range(len(prices)):
    total += prices[i]

print(f"The total price is ${total:,.2f}")