from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=.5,stretch_wid=.5)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):    
        x_random=random.randint(-250,250)
        y_random=random.randint(-250,250)
        self.goto(x_random,y_random)