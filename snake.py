from turtle import Turtle
SNAKE_STEP=20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
class Snake:
    def __init__(self):
        self.snakes=[]
        # self.length=3
        self.create_snake()
        self.head=self.snakes[0]

    def create_snake(self):  
        for  position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        square=Turtle(shape="square")
        square.color("white")
        square.penup()
        square.setpos(position)
        self.snakes.append(square)

    def extend(self):
        self.add_segment(position=self.snakes[-1].pos())    

    def reset_snake(self):
        for segment in self.snakes:
            segment.goto(1000,1000)
                
        self.snakes=[]
        self.create_snake()
        self.head=self.snakes[0]



    def move(self):
        for i in range(len(self.snakes)-1,0,-1):
            new_x=self.snakes[i-1].xcor()
            new_y=self.snakes[i-1].ycor()
            self.snakes[i].goto(new_x,new_y)
        self.head.forward(SNAKE_STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
              