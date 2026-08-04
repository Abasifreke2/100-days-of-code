import turtle
import pandas
# from create_state import State

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []
wrong_guesses = []
state = turtle.Turtle()
state.hideturtle()
state.penup()
state.pencolor("black")

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                    prompt="What's the name of another state? ")
    if answer_state.title() == "Exit":
        for state in states:
            if state not in guessed_states:
                wrong_guesses.append(state)
        df = pandas.DataFrame(wrong_guesses)
        df.to_csv("States_not_guessed.csv")
        break

    if answer_state.title() in states and answer_state.title() not in guessed_states :
        guessed_states.append(answer_state.title())
        state_data = data[data["state"] == answer_state.title()]
        x_axis = state_data["x"].item()
        y_axis = state_data["y"].item()
        state.goto(x=x_axis, y=y_axis)
        state.write(answer_state.title())




