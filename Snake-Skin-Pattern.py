
#importing the turtle module
import turtle

#creating the turtle object
turtle_obj = turtle.Turtle()

#setting the speed of the turtle
turtle_obj.speed(10)

#defining a function to create the snake skin pattern
def create_snake_skin_pattern():
  #looping through the sides of the pattern
  for i in range(6):
    #setting the color of the turtle
    turtle_obj.color('orange')
    #moving the turtle forward
    turtle_obj.forward(20)
    #turning the turtle right
    turtle_obj.right(60)
    #setting the color of the turtle
    turtle_obj.color('black')
    #moving the turtle forward
    turtle_obj.forward(20)
    #turning the turtle right
    turtle_obj.right(60)

#looping through the sides of the pattern
for i in range(15):
  #calling the function to create the snake skin pattern
  create_snake_skin_pattern()
  #turning the turtle left
  turtle_obj.left(30)

#hiding the turtle
turtle_obj.hideturtle()

#keeping the window open
turtle.done()