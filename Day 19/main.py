from turtle import Screen, exitonclick
from turtle import Turtle

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

screen.listen()
screen.onkey(key = 'space', fun= move_forward)
exitonclick()

# when we use a function as an argument(like pasing it to another function) then we don't add the parenthesis. what partenthtesis triggers the function to happen then and there, but what we want is for the function is wait till the space abr is pressed. and only when this happens we want it to trigger 
# thus when we pass function to another func we pass it as a name