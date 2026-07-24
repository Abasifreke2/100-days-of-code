from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.goto(-250, 270)
        self.write(f"Level: {self.score}", align="center", font=("Courier", 10, "normal"))


    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=FONT)