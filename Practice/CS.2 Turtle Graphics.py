import turtle

s = turtle.Screen()

t = turtle.Turtle()
t.pensize(3)

t.circle(100)

t.penup()
t.goto(-35, 120)
t.pendown()
t.dot(25)

t.penup()
t.goto(35, 120)
t.pendown()
t.dot(25)

t.penup()
t.goto(-60.2, 65)
t.pendown()
t.setheading(-60)
t.circle(70, 120)


turtle.done()
