# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Make sure to wear a jacket")
# else:
#     print("It's a lovely day")
# print("Enjoy your day")

house_price = int(input("House price: "))
credit_score = int(input("Buyer's credit score: "))
if credit_score >= 670 and credit_score < 851:
    print(f"The required down payment is ${(0.1 * house_price):,.2f}")
elif credit_score > 299 and credit_score < 670:
    print(f"The required down payment is ${(0.2 * house_price):,.2f}")
else:
    print("Invalid credit score entered. Try again")