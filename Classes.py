# classes have different naming conventions, if two words do this: PointClass

class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")


point1 = Point()
point1.draw()
point1.x = 10
point1.y = 20

point2 = Point()
point2.x = 1
print(point2.x)