from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.h_dir = 1
        self.v_dir = 1

    def move(self):
        if self.ycor() >= 289 or self.ycor() <= -280:
            self.bounce("wall")
        new_x = self.xcor() + self.h_dir
        new_y = self.ycor() + self.v_dir
        self.goto(x=new_x, y=new_y)

    def bounce(self, barrier):
        match barrier:
            case "wall":
                self.v_dir *= -1
            case "paddle":
                self.h_dir *= -1
                if self.h_dir > 0:
                    self.h_dir += 0.1
                else:
                    self.h_dir -= 0.1
                if self.v_dir > 0:
                    self.v_dir += 0.1
                else:
                    self.v_dir -= 0.1

    def reset(self):
        if self.xcor() > 0:
            self.h_dir = -1
        else:
            self.h_dir = 1
        self.v_dir = 1
        self.goto(0,0)