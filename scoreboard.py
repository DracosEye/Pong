from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = -1
        self.goto(x=pos[0], y=pos[1])
        self.add_point()

    def add_point(self):
        self.score += 1
        self.clear()
        self.write(self.score, font=("Arial", 75, "normal"))