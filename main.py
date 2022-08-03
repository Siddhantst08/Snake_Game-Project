from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("The Snake Game")

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game = True
while game:
    screen.update()
    time.sleep(0.09)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.inc_score()
    if snake.head.xcor() > 760 or snake.head.xcor() < -760 or snake.head.ycor() > 400 or snake.head.ycor() < -380:
        game = False
        scoreboard.game_over()
    for segment in snake.turtle_list[1:]:
        if snake.head.distance(segment) < 10:
            game = False
            scoreboard.game_over()

screen.exitonclick()
