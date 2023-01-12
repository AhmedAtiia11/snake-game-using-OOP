from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
# screen setup part
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)



snake=Snake()
Food=Food()
score=ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# goals=0


game_is_on=True
while game_is_on :
    screen.update()
    time.sleep(0.07)
    snake.move()

    if snake.head.distance(Food)<15:
        print("nom nom nom")
        Food.refresh()
        score.increase_score()
        snake.extend()

    for snakess in snake.snakes[1:]:
        if snake.head.distance(snakess)<10:
        #    score.game_over()
        #    game_is_on=False
            score.reset_score()
            snake.reset_snake() 

    if snake.head.xcor() >290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        # score.game_over()
        # game_is_on=False
        score.reset_score()
        snake.reset_snake()

screen.exitonclick()