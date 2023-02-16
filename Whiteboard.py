'''This code sets up a white board window with a turtle that can draw 
circles and lines. When the user clicks the screen, a circle is drawn at 
the mouse location. When the user presses the "c" key, the screen is 
cleared.
'''

import turtle

# Set up the turtle
turtle.setup(800, 600)  # Set the window size to 800x600 pixels
turtle.title("White Board")  # Set the window title to "White Board"
turtle.penup()  # Lift the pen up to prevent drawing
turtle.speed(0)  # Set the turtle speed to the fastest

# Define some functions for drawing
def draw_circle(x, y):
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(50)
    turtle.penup()

def draw_line(x1, y1, x2, y2):
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.penup()

# Set up the event listeners
turtle.onscreenclick(draw_circle)  # When the user clicks the screen, draw a circle at the mouse location
turtle.onkeypress(turtle.clear, "c")  # When the user presses the "c" key, clear the screen
turtle.listen()  # Start listening for events

# Run the turtle graphics loop
turtle.mainloop()
