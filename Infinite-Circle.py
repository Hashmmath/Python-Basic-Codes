'''When you run this code, it will create a Turtle object and set the pen color to blue. The draw_circle() function takes a radius parameter and uses the circle() method of the Turtle object to draw a circle of that radius.

The while loop will repeat indefinitely, continuously drawing circles of increasing size. The starting radius is set to 10, and then increased by 5 for each subsequent circle.

You can stop the program at any time by clicking on the Turtle graphics window and pressing the "Escape" key.'''
import turtle

# Create a Turtle object and set the pen color
t = turtle.Turtle()
t.pencolor("blue")

# Define a function to draw a circle of a given radius
def draw_circle(radius):
    t.circle(radius)

# Use a loop to repeatedly draw circles of increasing size
while True:
    radius = 10  # Starting radius
    draw_circle(radius)
    radius += 5  # Increase radius for the next circle
