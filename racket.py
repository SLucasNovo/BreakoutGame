from turtle import Turtle
SHAPESIZE = (1, 5)


class Racket(Turtle):
    '''This class defines the behaviour of the racket '''
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.ht()
        self.shapesize(SHAPESIZE[0], SHAPESIZE[1])
        self.color("white")
        self.setpos(0, -250)
        self.st()

    def lefter(self):
        new_x = self.xcor() - 40
        self.setposition(new_x, self.ycor())

    def righter(self):
        new_x = self.xcor() + 40
        self.setposition(new_x, self.ycor())
