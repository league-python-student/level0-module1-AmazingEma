# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr

import turtle
from tkinter import messagebox, simpledialog, Tk
import math
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    q = simpledialog.askinteger(title="", prompt="radius in pixels?")
    oq = simpledialog.askstring(title="", prompt="would you like to calculate area or circumference?")
    t = turtle.Turtle()
    t.circle(q)
    t.penup()
    t.goto(30, 90)
    if oq == 'area':
        Area = math.pi * q * q
        t.write("area = " + str(Area), move=True, align='left', font=('Arial', 8, 'normal'))
    else:
        circum = math.pi * 2 * q
        t.write('circum = ' + str(circum), move=True, align='left', font=('Arial', 8, 'normal'))
    t.hideturtle()
    turtle.done()
