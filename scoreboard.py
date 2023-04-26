from turtle import Turtle

class score(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color('white')
        self.score=0
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f'score is {self.score}', move=False, align='left', font=('Arial', 12, 'normal'))

    def increase(self):
        self.score+=10
        self.clear()
        self.update()

    def gameover(self):
        self.goto(-40, 0)
        self.write('Game Over', move=False, align='left', font=('Arial', 12, 'normal'))

