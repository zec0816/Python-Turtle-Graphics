import turtle
import random 

def flower():
    for i in range (300):
        r = random.randint(1,255)
        g = random.randint(1,255)
        b = random.randint(1,255)
        turtle.colormode(255)
        turtle.color(r,g,b)
        turtle.circle(190-i,90)
        turtle.left(90)
        turtle.circle(190-i,90)
        turtle.left(18)

turtle.bgcolor('black')
turtle.speed(1200)
flower()
turtle.mainloop()