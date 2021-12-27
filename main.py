from turtle import Turtle,Screen
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")

snake_game_on=False

snake=[]
post=[0,-20,-40]
for i in range(3):
    tim=Turtle()
    tim.color("white")
    tim.shape("square")
    tim.penup()
    tim.setposition(post[i],0)
    snake.append(tim)

       
        










screen.exitonclick()
