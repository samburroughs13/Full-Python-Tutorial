# numbers = [5,2,1,7,4]
# numbers.append(20)
# print(numbers)
# numbers.insert(0,20)
# print(numbers)
# print(numbers.index(1))
# print(numbers.count(20))
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers2 = numbers.copy()
# print(numbers2)

# Challenge
# Write a program to remove the duplicates in a list

numbers = [6,1,3,4,7,3,6,7,9,4,5,8,9,1,4,3,2,5,6,7]

# numbers.sort()
# for i in range(len(numbers)):
#     if i > len(numbers):
#         break
#     if numbers[i+1] == numbers[i] and not i > len(numbers):
#         while numbers[i+1] == numbers[i] and i+1 < len(numbers):
#             del numbers[i+1]
#             print(numbers)

numbers = list(set(numbers))

print(numbers)