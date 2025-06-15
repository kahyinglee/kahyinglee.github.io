import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")
t = turtle.Turtle()
t.color("red")

# Draw a heart
t.begin_fill()
t.left(50)
t.forward(100)
t.circle(40, 180)
t.left(260)
t.circle(40, 180)
t.forward(100)
t.end_fill()

# Write message
t.penup()
t.goto(0, -50)
t.color("black")
t.write("I ❤️ Dad", align="center", font=("Arial", 24, "bold"))
turtle.done()
