from turtle import Turtle , Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"A")
screen.onkeypress(l_paddle.go_down,"Z")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset_ball()
        score.l_point()
        score.update_scoreboard()

    if ball.xcor() < -400:
        ball.reset_ball()
        score.r_point()
        score.update_scoreboard()


screen.exitonclick()
