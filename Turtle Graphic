import colorgram
from turtle import Turtle,Screen,exitonclick
import turtle as t
import random

color_tuple = ()

def random_color():
    global color_tuple
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    color_tuple = (r,b,g)
    return color_tuple

def draw_spiral(size_of_gap):
    for x in range(360 // size_of_gap):
        jeff.color(random_color())
        jeff.circle(100)
        jeff.setheading(jeff.heading() + size_of_gap)


t.colormode(255)

screen = Screen()

jeff = Turtle()
jeff.shape('turtle')
jeff.pensize(1)

jeff.speed(0)


draw_spiral(1)




exitonclick()

colors = ["blue","green","black","brown","red","yellow","pink","purple","teal","gray","beige"]

done = True
screen = Screen()

jeff = t()

dot_size = 20
dot_distance = 50

jeff.shape("turtle")
jeff.penup()
jeff.goto(-350,200)

jeff.speed(0)
jeff.forward(100)


for row in range(10):
    for column in range(10):
        jeff.pencolor(random.choice(colors))
        jeff.dot(dot_size)
        jeff.forward(dot_distance)
    jeff.backward(dot_distance * 10)
    jeff.right(90)
    jeff.forward(dot_distance)
    jeff.left(90)
