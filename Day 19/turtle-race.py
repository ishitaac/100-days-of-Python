from turtle import Turtle
from turtle import Screen
from turtle import exitonclick
import random

is_race_on = False
screen = Screen()
screen.setup(width= 500, height=400)
user_bet = screen.textinput(title = "Make your bet", prompt=" Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red","orange","yellow","green","blue","purple"]
y_pos = [-70,-40,-10,20,50,80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x= -230,y= y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations you have won! Color {winning_color} is the winner")
            else:
                print(f"You have lost the bet, color {winning_color} won the race!")


        ran_distance = random.randint(0,10)
        turtle.forward(ran_distance)



screen.exitonclick()