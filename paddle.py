from turtle import Turtle


class Paddle (Turtle):

    def __init__(self, coords):
        super().__init__(shape="square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coords[0], coords[1])

    def move_up(self):
        if self.ycor() < 240:
            self.goto(x=self.xcor(), y=self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -240:
            self.goto(x=self.xcor(), y=self.ycor() - 20)