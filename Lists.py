# Given a list of numbers, find the largest number in the list

numbers = [1, 4, 5, 7, 3, 2, 8, 9, 6]
largest_number = numbers[0]

for i in range(len(numbers)):
    if numbers[i] > largest_number:
        largest_number = numbers[i]

print(f"The largest number is {largest_number}")