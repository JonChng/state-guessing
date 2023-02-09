import turtle
import pandas as pd
from string import capwords
from state import State

df = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"

screen.addshape("blank_states_img.gif")
turtle.shape(image)

game_is_on = True
guesses = []
count = 0

while game_is_on:
    answer_state = screen.textinput(f"{count}/50 States Correct", "What is your answer? ")

    guess = capwords(answer_state)
    states = df["state"].to_list()

    if guess in guesses:
        print("You have already guessed this.")
        continue

    else:
        guesses.append(guess)

    if guess in states:
        x = df[df["state"] == guess]['x'].values[0]
        y = df[df["state"] == guess]['y'].values[0]
        count += 1
        state = State(x, y, guess)

    if count == 50:
        game_is_on = False


screen.exitonclick()