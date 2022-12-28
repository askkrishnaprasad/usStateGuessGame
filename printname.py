from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Printname(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()

    def update_state(self, x_pos, y_pos, state):
        self.goto(x_pos, y_pos)
        self.write(state, align=ALIGNMENT, font=FONT)
