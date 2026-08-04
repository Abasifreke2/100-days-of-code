from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        with open("data.txt",mode="r") as data:
            self.high_score = int(data.read())
        self.goto(0,270)
        self.write(f"Score:{self.score} High Score:{self.high_score}" , align="center",font=('Arial', 8, 'normal'))

    def reset_score(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as self.high_score:
                self.high_score.write(str(self.score))

            with open("data.txt", mode="r") as data:
                self.high_score = int(data.read())

        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:{self.high_score}",
                   align="center",
                   font=("Arial", 8, "normal"))
