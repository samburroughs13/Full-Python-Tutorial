# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True
# }
#
# print(customer["name"])
# print(customer.get("name"))
# print(customer.get("birthdate", "Jan 1 1980"))
#
# customer["name"] = "Jack Smith"
# print(customer["name"])

# Exercise
# ask for phone number, then return the numbers that the user input as words
# input: 1234
# output: One Two Three Four

numbers = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

user_num = input("Phone: ")
output_string = ""

for i in range(len(user_num)):
    output_string += numbers.get(user_num[i]) + " "

print(output_string)