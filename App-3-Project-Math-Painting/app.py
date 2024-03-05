import streamlit as st
import numpy as np
from PIL import Image

class Square:
    def __init__(self, x, y, side, color):
        self.x = int(x)
        self.y = int(y)
        self.side = int(side)
        self.color = color

    def draw_square(self, canvas):
        canvas.data[self.x:self.x+self.side, self.y:self.y+self.side] = self.color

class Rectangle:
    def __init__(self, x, y, length, width, color):
        self.x = int(x)
        self.y = int(y)
        self.length = int(length)
        self.width = int(width)
        self.color = color

    def draw_rectangle(self, canvas):
        canvas.data[self.x:self.x+self.length, self.y:self.y+self.width] = self.color

class Canvas:
    def __init__(self, width, height, color):
        self.width = int(width)
        self.height = int(height)
        self.color = color

        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        self.data[:] = self.color
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def draw_canvas(self):
        for shape in self.shapes:
            if isinstance(shape, Square):
                shape.draw_square(self)
            elif isinstance(shape, Rectangle):
                shape.draw_rectangle(self)
        img = Image.fromarray(self.data, 'RGB')
        return img

def main():
    st.title("Canvas Drawing App")

    canvas_width = st.slider("Enter the width of the canvas:", 100, 1000, 500)
    canvas_height = st.slider("Enter the height of the canvas:", 100, 1000, 500)
    canvas_color = st.radio("Enter the color of the canvas:", ("White", "Black"))

    if canvas_color == "White":
        canvas_color = (255, 255, 255)
    else:
        canvas_color = (0, 0, 0)

    canvas = Canvas(canvas_width, canvas_height, canvas_color)


    shape = st.selectbox("Select the shape you want to draw:", ("Square", "Rectangle", "Quit"))

    if shape == "Square":
        x = st.number_input("Enter the x coordinate of the square:")
        y = st.number_input("Enter the y coordinate of the square:")
        side = st.number_input("Enter the side of the square:")
        red = st.slider("Red:", 0, 255, 0)
        green = st.slider("Green:", 0, 255, 0)
        blue = st.slider("Blue:", 0, 255, 0)
        color = (red, green, blue)

        square = Square(x, y, side, color)
        canvas.add_shape(square)
        st.image(canvas.draw_canvas(), caption='Canvas with Shapes')

    elif shape == "Rectangle":
        x = st.number_input("Enter the x coordinate of the rectangle:")
        y = st.number_input("Enter the y coordinate of the rectangle:")
        length = st.number_input("Enter the length of the rectangle:")
        width = st.number_input("Enter the width of the rectangle:")
        red = st.slider("Red:", 0, 255, 0)
        green = st.slider("Green:", 0, 255, 0)
        blue = st.slider("Blue:", 0, 255, 0)
        color = (red, green, blue)

        rectangle = Rectangle(x, y, length, width, color)
        canvas.add_shape(rectangle)
        st.image(canvas.draw_canvas(), caption='Canvas with Shapes')

    elif shape == "Quit":
        st.write("Thank you for using the app!")


if __name__ == "__main__":
    main()
