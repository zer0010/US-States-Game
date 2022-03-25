import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
temp_list = data['state'].to_list()
guessed_state = []

while len(guessed_state) < 50:

    answer_state = screen.textinput(title=f'Score: {len(guessed_state)}/50', prompt="What's another State name?").title()

    if answer_state == 'Exit':
        break
    if answer_state in temp_list:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        get_xy = data[data.state == answer_state]
        t.goto(int(get_xy.x), int(get_xy.y))
        t.write(answer_state)
turtle.mainloop()

