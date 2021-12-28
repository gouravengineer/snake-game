from turtle import Turtle,Screen
from snake import Snake
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")

snake_game_on=False
screen.tracer(0)        #It is used to turn off animation when arg*=0
snake=Snake()

screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.right,key="Right")
screen.onkey(fun=snake.left,key="Left")
snake_game_on=True
while snake_game_on:    #The while loop is used to move forward
    time.sleep(0.1)
    screen.update()
    snake.move()
    


        
    
       
        










screen.exitonclick()
