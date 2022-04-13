import turtle


this_turtle = turtle.Turtle()
this_turtle.color("black", "blue")

this_turtle.begin_fill()
for x in range(4):
  this_turtle.forward(120)
  this_turtle.right(90)
this_turtle.end_fill()

this_turtle.forward(100)
this_turtle.color("black", "white")

this_turtle.begin_fill()
for x in range(4):
  this_turtle.forward(120)
  this_turtle.right(90)
this_turtle.end_fill()

this_turtle.forward(100)
this_turtle.color("black", "red")

this_turtle.begin_fill()
for x in range(4):
  this_turtle.forward(120)
  this_turtle.right(90)
this_turtle.end_fill()