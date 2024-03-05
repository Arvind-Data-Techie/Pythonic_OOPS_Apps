import math
import turtle


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_Rectangle(self, rectangle):
        print(rectangle.lowleft.x, '<', self.x, '<', rectangle.upright.x)
        print(rectangle.lowleft.y, '<', self.y, '<', rectangle.upright.y)
        if rectangle.lowleft.x < self.x < rectangle.upright.x and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False

    def get_distance(self, point_1, point_2):
        return math.sqrt((point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y) ** 2)


class Rectangle:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def get_area(self):
        length = self.upright.x - self.lowleft.x
        width = self.upright.y - self.lowleft.y
        area = length * width
        return area


class GUIRectangle(Rectangle):

    def add_graph(self, my_turtle):
        print('Inside GUI', my_turtle)
        my_turtle.penup()
        my_turtle.goto(self.lowleft.x, self.lowleft.y)
        my_turtle.pendown()

        length = self.upright.x - self.lowleft.x
        width = self.upright.y - self.lowleft.y

        my_turtle.forward(length)
        my_turtle.left(90)
        my_turtle.forward(width)
        my_turtle.left(90)
        my_turtle.forward(length)
        my_turtle.left(90)
        my_turtle.forward(width)


class Guipoint(Point):

    def draw_point(self, my_turtle, size=5, colour='red'):
        my_turtle.penup()
        my_turtle.goto(self.x, self.y)
        my_turtle.pendown()
        my_turtle.dot(size, colour)






x = int(input('Enter x-coordinate : '))
y = int(input('Enter y-coordinate : '))
input_point = Point(x,y)

gui_object = GUIRectangle(Point(0,0), Point(100,100))  # can be random points

print('The given Point Falls inside Rectangle : ',input_point.falls_in_Rectangle(gui_object))


my_turtle = turtle.Turtle()
gui_object.add_graph(my_turtle)

user_point=Guipoint(x,y)

user_point.draw_point(my_turtle)

turtle.done()
