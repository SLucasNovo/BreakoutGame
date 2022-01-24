from turtle import Turtle
STARTING_POSITION = (-100, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.shape_scoreboard()
        self.mark_score(self.points)

    def mark_score(self, points):
        self.clear()
        self.write(f"Points : {points}", False, align="center", font=('Arial', 24, 'normal'))

    def shape_scoreboard(self):
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(STARTING_POSITION)

    def game_over(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 0)
        self.write("GAME OVER\nTry again? y/n", False, align="center", font=('Arial', 24, 'normal'))
        # event listener try again

    def win(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 0)
        self.write("Congratulations you won!\nTry again? y/n", False, align="center", font=('Arial', 24, 'normal'))