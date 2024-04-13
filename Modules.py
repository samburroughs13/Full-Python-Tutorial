# import converters
#
# # you can use this method to import just one function from the module
#
# from converters import kg_to_lbs
#
# # when you specifically import the function, you don't have to type modulename.function(), you can just do function()
#
# print(kg_to_lbs(100))
#
# print(converters.kg_to_lbs(70))

# Exercise
# Take the code that I made to find the max number in a list, put it in a function called find_max within a module called utils

import utils

print(utils.find_max([1,5,6,4,8]))