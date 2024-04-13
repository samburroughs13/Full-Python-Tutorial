# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")
#
#
# point1 = Point(10,20)
# point1.x = 11
# print(point1.x)

# Exercise
# define a new object called Person with a name attribute and a talk() method

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi my name is {self.name}")


person1 = Person("Bob")
person1.talk()

person2 = Person("John")
person2.talk()