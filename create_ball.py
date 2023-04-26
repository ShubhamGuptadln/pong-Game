from turtle import Turtle


class create(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')


        self.color('blue')

        self.penup()
        self.x_move=10
        self.y_move=10
        self.movespeed=0.1





    def refresh(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce(self):
        self.y_move*=-1

    def bounce_back(self):
        self.x_move*=-1
        self.movespeed*=0.9

    def setback(self):
        self.goto(0,0)
        self.x_move*=-1






