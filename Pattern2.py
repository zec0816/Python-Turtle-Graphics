import turtle

t = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor('black')
t.color('orange')
t.speed(20)

for i in range(90):
    t.right(i)
    t.circle(200,i)
    t.forward(i)
    t.right(90)
    t.forward(i)

t.hideturtle()
wn.exitonclick()