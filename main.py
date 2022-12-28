from turtle import Turtle, Screen
import pandas

from printname import Printname

screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
back_image = Turtle()
back_image.shape(image)
printname = Printname()

data = pandas.read_csv("50_states.csv")

i = 0
while i < 50:
    answer_text = screen.textinput(title="Guess the state", prompt="Enter a US State")
    answer_text = answer_text.title()
    gray_squirrels_count = len(data[data.state == answer_text])
    if gray_squirrels_count != 0:
        i = i + 1
        coordinates = data[data.state == answer_text]
        x_pos = coordinates.x
        y_pos = coordinates.y
        printname.update_state(int(x_pos), int(y_pos), answer_text)
    else:
        printname.update_state(0, 100, "State Not in US :)")

screen.exitonclick()
