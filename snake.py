from turtle import Turtle,Screen
import random
Random_value=[-280, -270, -260, -250, -240, -230, -220, -210, -200, -190, -180, -170, -160, -150, -140, -130, -120, -110, -100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280]
STARTING_POSITION=[(0,0),(-10,0),(-20,0),(-30,0)]
MOVE_DISTANCE=10
up=90
down=270
left=180
right=0

class Snake():
    def __init__(self):
        self.snake_body=[]
        self.create_snake()
        self.head=self.snake_body[0]

    def create_snake(self):
        for data in STARTING_POSITION:
                self.add_segment(data)    
    def add_segment(self,data):
        tim=Turtle()
        tim.color("white")
        tim.shape("square")
        tim.shapesize(0.5,0.5)
        tim.penup()
        tim.setposition(data)
        self.snake_body.append(tim)
    def extend(self):
        self.add_segment(self.snake_body[-1].position())
    def move(self):
        for i in range(len(self.snake_body)-1,0,-1):
            x=self.snake_body[i-1].xcor()
            y=self.snake_body[i-1].ycor()
            self.snake_body[i].goto((x,y))
            
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)
                

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def right(self):
        if self.head.heading() !=left :
            self.head.setheading(right)
    def left(self):
        if self.head.heading() !=right :
            self.head.setheading(left)

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.6,stretch_wid=0.6)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        random_x=(random.choice(Random_value)//10)*10
        random_y=(random.choice(Random_value)//10)*10
        self.goto(random_x,random_y)
Font=("Courier",15,"normal")
Alignment="center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(0,275)
        self.write(f"Score: {self.score}", align=Alignment,font=Font)
    def game_over(self):
        self.setposition(0,0)
        self.write("GAME OVER!", align=Alignment,font=Font)
        self.setposition(0,-20)
        self.write("Press space to restart", align=Alignment,font=Font)
    def clear_score(self):
        self.score = 0
    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}", align=Alignment,font=Font)

#class newgame(Screen):
#	def __init__(self):
#		super().__init__()
#	def new(self):
#		self.clearscreen()
		
