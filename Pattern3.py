from turtle import *
import random 

speed(200)
colormode(255)
bgcolor('black')

for i in range(120):
    color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    for j in range(2):
        fd(i)
        lt(60)
        rt(120)
    rt(240)
    lt(51)
    circle(3)
done()