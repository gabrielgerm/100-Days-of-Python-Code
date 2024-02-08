import turtle
import pandas

def write_state_name(state_name, x, y):
    new_state_name = turtle.Turtle()
    new_state_name.hideturtle()
    new_state_name.penup()
    new_state_name.goto((x, y))
    new_state_name.write(state_name, align="center", font=('Arial', 8, 'normal'))
    
screen = turtle.Screen()
screen.setup(width=730, height=495)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.Turtle().shape(image)

us_data = pandas.read_csv("50_states.csv")
us_states_list = us_data.state.to_list()

correct_guesses = []
while len(correct_guesses) < 50:
    screen.title(f"U.S States Game  - {len(correct_guesses)}/50")
    user_guess = turtle.textinput(title="U.S States Game", prompt="Make your guess!").title()
    if user_guess == "Exit":
        break
    else:
        if user_guess not in correct_guesses:
            if user_guess in us_states_list:
                correct_guesses.append(user_guess)
                state_info = us_data[us_data.state == user_guess]
                write_state_name(user_guess, int(state_info.x), int(state_info.y))

states_to_learn = []
for state in us_states_list:
    if state not in correct_guesses:
        states_to_learn.append(state)
pandas.DataFrame(states_to_learn).to_csv("states_to_learn.csv")
screen.mainloop()