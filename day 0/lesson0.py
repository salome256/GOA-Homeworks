from turtle import *


#we want to paint a house

#step1: drow ascvare
speed(5)
width("7")
color("purple")

forward(200)
left(90)
 
forward(200)
left(90)

forward(200)
left(90)
 
forward(200)
left(90)
#ensd of squar

#drowing a door



forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


penup()
goto(135, 135)
pendown()
color("brown")
begin_fill()
right(60)
forward(70)
right(90)
forward(50)
right(90)
forward(70)
right(90)
forward(50)
end_fill()

exitonclick()