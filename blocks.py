from turtle import Turtle
import random

COLORS = ['green', 'yellow', 'orange', 'red']
SIZE_MAX = 30
SIZE_MIN = 15
HEIGHT = 15


class Blocks(Turtle):
    '''This class defines the behaviour of a single block'''
    def __init__(self, color, position_x, position_y):
        super().__init__()
        self.single_block(color, position_x, position_y)
        self.row = []
        self.rows = []
        self.row_y = 60

    def single_block(self, color, position_x, position_y):
        self.penup()
        self.shape("square")
        self.hideturtle()
        self.color(color)
        self.turtlesize(1, 2)
        self.goto(position_x, position_y)
        self.showturtle()

    def delete_block(self):
        self.penup()
        self.hideturtle()
        self.goto(800, 800)

    def row_blocks(self):
        for color in COLORS:
            for step in range(-350, 400, 50):
                self.row.append(self.single_block(color, step, self.row_y ))
            self.rows.append(self.row)
            self.row_y += 60
