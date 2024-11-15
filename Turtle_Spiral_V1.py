import turtle

#background and pen properties
turtle.bgcolor('#add8e6')
turtle.pensize(2)

#colours 
colors = ["blue", "yellow", "green", "red"]

#starting position at the origin
turtle.penup()
turtle.setpos(0,0)
turtle.pendown()

#main drawing loop
for i, color in enumerate(colors * 3): # Repeat colours to get a longer shape
    turtle.pencolor(color)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(50)
    turtle.left(120)
    turtle.left(30) # For spiral effect

turtle.exitonclick()