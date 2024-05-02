from turtle import Turtle, Screen, exitonclick
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)


user_bet = screen.textinput(title="Make your bet!",prompt="Which colored turtle will win?: ")
print(user_bet)

if len(user_bet) == 0:
    is_race_on = False
else:
    is_race_on = True



colors = ["red","blue","black","green","purple","orange"]
all_turtles = []

z = -100


for x in range(6):
    new_turtle = Turtle()
    all_turtles.append(new_turtle)
    new_turtle.shape("turtle")
    new_turtle.color(colors[x])
    new_turtle.penup()
    new_turtle.goto(-235,z)
    z = z + 25


while is_race_on:
    new_turtle.speed(1)
    for turtle in all_turtles:
        turtle.forward(random.randint(0,10))
    for z in all_turtles:
        if z.xcor() > 220:
            winner_color = z.color()
            if user_bet == winner_color[0]:
                print("Congrats your turtle won!")
            else:
                print(f"{winner_color[0]} is the winner!")
            is_race_on = False
