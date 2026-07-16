from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Welcome to my snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scores = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_running = True
while game_is_running:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food an update score
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scores.score += 1
        scores.clear()
        scores.update_scoreboard()

#detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_running = False
        scores.game_over()

    # detect collision with the tail

    for segment in snake.segments[2:]:
        if snake.head.distance(segment) < 10:
            game_is_running = False
            scores.game_over()


screen.exitonclick()