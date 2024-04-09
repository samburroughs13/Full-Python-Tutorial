# Using nested loops, draw this F shape:
# xxxxx
# xx
# xxxxx
# xx
# xx

numbers = [5,2,5,2,2]

for i in range(len(numbers)):
    for j in range(numbers[i]):
        print("x", end='')
    print("")

# use the same method to print an L

print("")
numbers = [2,2,2,2,5]

for i in range(len(numbers)):
    for j in range(numbers[i]):
        print("x", end='')
    print("")