import numpy as np
from PIL import Image

class Square:
    def __init__(self,x,y,side,color):
        self.x = x
        self.y = y
        self.side=side
        self.color = color


    def draw_square(self,canvas):
        canvas.data[self.x:self.x+self.side, self.y:self.y+self.side] = self.color




class Rectangle:
    def __init__(self, x,y,length,width,color):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.color = color



    def draw_rectangle(self,canvas):
        canvas.data[self.x:self.x+self.length, self.y:self.y+self.width] = self.color

class Canvas:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # create a 3d numpy array of zeros
        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        self.data[:] = self.color


    def draw_canvas(self):
        img=Image.fromarray(self.data, 'RGB')
        img.save('my.png')
        return self.data




canvas_width= int(input("Enter the width of the canvas: "))
canvas_height= int(input("Enter the height of the canvas: "))
canvas_color= input("Enter the color of the canvas - white/black : ")

if canvas_color=='white':
    canvas_color=(255,255,255)
else:
    canvas_color=(0,0,0)
canvas=Canvas(canvas_width,canvas_height,canvas_color)

flag=True
while flag:

    shape=input("Enter the shape you want to draw - square/rectangle Or do you want to quit? : ")

    if shape=="square":
        x=int(input("Enter the x coordinate of the square: "))
        y=int(input("Enter the y coordinate of the square: "))
        side=int(input("Enter the side of the square: "))
        color=input("How Much Red,Green, Blue do you want in the square? Eg: 255,255,255 for white: ")
        red=int(color[:3])
        green=int(color[4:7])
        blue=int(color[8:11])
        color=(red,green,blue)
        square=Square(x,y,side,color)
        square.draw_square(canvas)
        canvas.draw_canvas()
        print('Square Drawn!!!! Next Shape Please')
    elif shape=="rectangle":
        x=int(input("Enter the x coordinate of the rectangle: "))
        y=int(input("Enter the y coordinate of the rectangle: "))
        length=int(input("Enter the length of the rectangle: "))
        width=int(input("Enter the width of the rectangle: "))
        color=input("How Much Red,Green, Blue do you want in the rectangle? Eg: 255,255,255 for white: ")
        red=int(color[:3])
        green=int(color[4:7])
        blue=int(color[8:11])
        color=(red,green,blue)
        rectangle=Rectangle(x,y,length,width,color)
        rectangle.draw_rectangle(canvas)
        canvas.draw_canvas()
        print('Rectangle Drawn!!!! Next Shape Please')

    elif shape=="quit":
        flag=False
        print("Thank you for using the app!")







