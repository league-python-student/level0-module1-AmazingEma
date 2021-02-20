import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    t = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title="", prompt="circle, square, or triangle?")
    # Draw the shape requested by the user using if-elif-else statements
    if shape == "circle":
        t.speed(0)
        t.circle(50, 360,12292)
    elif shape == "square":
        t.circle(50,360,4)
    else:
        t.circle(50,360,3)
    # Call the turtle .done() method
turtle.done()