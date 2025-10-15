from turtle import Turtle



class Paddle(Turtle):


    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.speed('fastest')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.setpos(position)


    def go_up(self):
       self.goto(self.xcor(), self.ycor() + 30)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 30)