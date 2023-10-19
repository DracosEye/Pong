from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
game_over = False

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Classic Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
left_score = Scoreboard((-210, 205))
right_score = Scoreboard((210, 205))

screen.listen()
screen.onkey(right_paddle.move_up, 'Up')
screen.onkey(right_paddle.move_down, 'Down')
screen.onkey(left_paddle.move_up, 'w')
screen.onkey(left_paddle.move_down, 's')

while not game_over:
    screen.update()
    if (ball.xcor() >= 340 and ball.distance(right_paddle) <= 50 or
            ball.xcor() <= -340 and ball.distance(left_paddle) <= 50):
        ball.bounce("paddle")
    ball.move()
    if ball.xcor() >= 345:
        ball.reset()
        left_score.add_point()
        if left_score.score >= 11 and left_score.score - right_score.score > 1:
            game_over = True
    elif ball.xcor() <= -345:
        ball.reset()
        right_score.add_point()
        if right_score.score >= 11 and right_score.score - left_score.score > 1:
            game_over = True

screen.exitonclick()