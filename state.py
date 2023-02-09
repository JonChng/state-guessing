from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

class State(Turtle):

    def __init__(self, x, y, state):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(state, align= ALIGNMENT, font = FONT)

