import random


# for i in range(3):
#     print(random.randint(10,20))
#
# members = ["John", "Mary", "Bob"]
# print(random.choice(members))

# Exercise
# Make a class called Dice with method roll, which generates a tuple with two random values from 1 to 6


class Dice:
    sides = int(input("How many sides on the dice? "))

    def roll(self):
        return random.randint(1, self.sides), random.randint(1, self.sides)


dice1 = Dice()
print(dice1.roll())
