from turtle import Screen
from racket import Racket
from ball import Ball
from blocks import Blocks
from score import Scoreboard
import time

COLORS = ['green', 'yellow', 'orange', 'red']

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Breakout Game")
screen.tracer(0)

ball = Ball()
racket = Racket()
score = Scoreboard()
# ---------------------------------- Functions for game


def create_rows():
    global row_y, rows
    for color in COLORS:
        row = []
        for step in range(-350, 400, 50):
            row.append(Blocks(color, step, row_y))
        rows.append(row)
        row_y += 60


def quit_game():
    screen.bye()


def start_game():
    global rows, row_y
    rows = []
    row_y = 0
    create_rows()
    ball.goto(0, 0)


screen.listen()
screen.onkey(racket.lefter, 'Left')
screen.onkey(racket.righter, 'Right')
screen.onkey(start_game, 's')
screen.onkey(quit_game, 'q')


rows = []
row_y = 0
game_is_on = True


# ---------------------------------- Game

create_rows()


while game_is_on:

    screen.update()
    time.sleep(0.1)
    ball.move_ball()

    # Detect collision with racket
    if ball.distance(racket) < 35 and ball.ycor() < 220 or ball.ycor() > 295:
        ball.y_bounce()

    # Detect wall collision
    if ball.xcor() >= 395 or ball.xcor() <= -395:
        ball.x_bounce()

    # Detect block and ball collision
    for row in rows:
        for block in row:
            if 25 >= ball.distance(block) >= 23:
                print(ball.distance(block))
                ball.x_bounce()
                block.delete_block()
                score.mark_score(score.points)
                score.points += 1

            elif ball.distance(block) <= 23:
                ball.distance(block)
                ball.y_bounce()
                block.delete_block()
                score.mark_score(score.points)
                score.points += 1

    if not rows:
        score.win()

    if ball.ycor() <= -390:
        game_is_on = False
        score.game_over()



screen.mainloop()
