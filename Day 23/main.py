import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(turtle.move_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()
    if turtle.finish_line():
        score.update_scoreboard()
        cars.increase_speed()
    for car in cars.all_cars:
        if turtle.distance(car) < 28:
            game_is_on = False
            score.game_over()





screen.exitonclick()
