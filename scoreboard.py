from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        # self.high_score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        with open("scores.txt",mode="r")as file:
            result=file.read()
            self.high_score=int(result)
            print(self.high_score)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score={self.score} High Score is {self.high_score}",align="center",font=('Arial',24, 'normal'))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()

    def reset_score(self):
        if self.score>self.high_score:
            with open("scores.txt",mode="w")as file:
                self.high_score=self.score
                file.write(f"{self.high_score}")
        self.score=0
        self.update_score()

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("Game Over",align="center",font=("Arial",24,"normal"))
        self.hideturtle()