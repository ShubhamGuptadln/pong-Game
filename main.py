import turtle
from turtle import Turtle, Screen
from paddle import Paddle
from create_ball import create
from scoreboard import score
import time
s = Screen()
s.tracer(0)
t = Turtle()

turtle.bgcolor('black')
turtle.setup(width=800, height=600)
pad_right = Paddle((350, 0))
pad_left = Paddle((-350, 0))


s.listen()
s.onkey(fun=pad_right.up_right, key='Up')
s.onkey(fun=pad_right.down_right, key='Down')
s.onkey(fun=pad_left.up_left, key='w')
s.onkey(fun=pad_left.down_left, key='s')

t.color('white')
t.penup()
t.goto(0, 300)
t.right(90)

for i in range(300):
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(10)

game_is_on = True
c = create()
sc_left=score((-100,280))
sc_right=score((100,280))

while game_is_on:
    s.update()
    time.sleep(c.movespeed)
    c.refresh()

    if c.ycor()>280 or c.ycor()<-280:
        c.bounce()
    if pad_left.distance(c)<=50 and pad_left.xcor()<-340 :
        c.bounce_back()


    if pad_right.distance(c)<=50 and pad_right.xcor()>340:
        c.bounce_back()


    if c.xcor()>=380 :
        c.setback()
        sc_left.increase()

    if c.xcor()<=-380:
        c.setback()
        sc_right.increase()








s.exitonclick()
