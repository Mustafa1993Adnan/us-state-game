import turtle
import pandas

screen = turtle.Screen()
screen.title("US map")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
data_states = pandas.read_csv("50_states.csv")
all_states = data_states.state.to_list()
guessed_states = []
not_guessed = []
while len(guessed_states) < 50:
    user_input = turtle.textinput(f"Enter state", f"{len(guessed_states)}/50 Guess another state?").title()

    if user_input == 'Exit' or user_input is None:
        print(guessed_states)
        not_guessed = [notGuest for notGuest in all_states if notGuest not in guessed_states]
        print(not_guessed)
        final_list = pandas.DataFrame(not_guessed)
        final_list.to_csv('not_guessed_file.csv')
        break
    if user_input in all_states:
        guessed_states.append(user_input)
        row_data = data_states[data_states.state == user_input]
        pen.goto(int(row_data.x), int(row_data.y))
        pen.write(user_input)
    # if user_input in all_states:
    #     guessed_states.append(user_input)
    #     row_data = data_states[data_states.state == user_input]
    #     pen.goto(int(row_data.x), int(row_data.y))
    #     pen.write(user_input)
# for item in all_states:
#     if item not in guessed_states:
#         not_guessed.append(item)

