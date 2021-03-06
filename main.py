from turtle import Turtle,Screen
from snake import Snake,Food,Scoreboard
import time
screen=Screen()

def main():
	score=Scoreboard()

	screen.setup(width=600,height=600)
	screen.bgcolor("black")

	snake_game_on=False
	screen.tracer(0)        #It is used to turn off animation when arg*=0
	snake=Snake()
	food=Food()
	screen.listen()
	screen.onkey(fun=snake.up,key="Up")
	screen.onkey(fun=snake.down,key="Down")
	screen.onkey(fun=snake.right,key="Right")
	screen.onkey(fun=snake.left,key="Left")
	screen.onkey(fun=None,key="space")
	snake_game_on=True
	while snake_game_on:    #The while loop is used to move forward
		def restart():
			screen.clear()
			main()
		time.sleep(0.055)
		screen.update()
		snake.move()
		
		#detect collision with food
		if snake.head.distance(food)<12:
			food.refresh()
			snake.extend()
			score.increase_score()
		#detect collision with wall
		if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
			snake_game_on=False
			score.game_over()
			#screen.clear()
			screen.onkey(fun=restart, key="space")
			

		#detect collision with self
		for segment in snake.snake_body[1:]:
			if snake.head.distance(segment)<5:
				snake_game_on=False
				print("hello world")
				score.game_over()
		#if head=snake_body[0] collides with any of the segment
		#trigger game over

	
	   
	

main()








screen.exitonclick()
