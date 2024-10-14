"""
Write a class called Point that accepts an x and y values for two ordered pairs from the user
representing two points on the coordinate plane.

Implement two methods:
    1) The first method returns a new ordered pair that represents the difference between
        the x and y values of the two points.

        For example if the points are (3,5) and (-1,10) we will return (x2-x1,y2-y1)
                    ...(-2-3, 10-5) = (-5, 5)
                    So we would return (-5 and 5 in this case.

    2) The second method returns a Pythagoran distance of the two points.
                For example: if the points are (3,5) and (-1,10), we can do:

                    √((y2-y1)^2 + (x2-x1)^2) = √((10-5)^2 + (-1-3)^2)
                    = √(5^2 + (-4)^2) = √(25 +16) = √41 = 6.4

    Show that your methods work by creating a class and utilizing them.
"""
class Point:
    def __init__(self, x1,x2,y1,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


    def difference(self):
        new_point = (self.x2-self.x1, self.y2-self.y1)
        return new_point


    def pyth_dist(self):
        dist = ((self.y2-self.y1) **2) + ((self.x2-self.x1)**2)
        dist = dist **0.5
        return dist

x1 = int(input("Enter the value of x1: "))
y1 = int(input("Enter the value of y1: "))
x2 = int(input("Enter the value of x2: "))
y2 = int(input("Enter the value of y2: "))

p1 = Point(x1,x2,y1,y2)
print(p1.difference())
print(p1.pyth_dist())
