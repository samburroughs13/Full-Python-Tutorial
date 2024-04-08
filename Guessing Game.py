import random

number = random.randint(1, 10)
guess = 0
i = 0
while i < 3:
    guess = int(input("Guess a number 1 through 10: "))
    if guess == number:
        print("Correct!")
        break
    i += 1
else:
    print("Three guesses exceeded")