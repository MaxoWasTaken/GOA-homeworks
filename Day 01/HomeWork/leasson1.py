from turtle import *

#we want to paint a house

#step 1: draw a square

penup()
goto(-300, -350)
pendown()

width(7)
color("purple")
begin_fill()
forward(400)
left(90)

forward(400)
left(90)

forward(400)
left(90)

forward(400)
left(90)
end_fill()
#end of square

#drawing a door

forward(140)
color("brown")
begin_fill()
left(90)
forward(240)    #height of the door
right(90)
forward(120)
right(90)
forward(240)
end_fill()

penup()
goto(100, 50)
pendown()

color("red")
begin_fill()
right(150)
forward(400)
left(120)
forward(400)
end_fill()

#drawing windows

penup()
goto(-270, -280)
pendown()

color("blue")
begin_fill()
right(150)
forward(140)
right(90)
forward(90)
right(90)
forward(140)
right(90)
forward(90)
end_fill()

penup()
goto(-20, -280)
pendown()

color("blue")
begin_fill()
right(90)
forward(140)
right(90)
forward(90)
right(90)
forward(140)
right(90)
forward(90)
end_fill()









exitonclick()