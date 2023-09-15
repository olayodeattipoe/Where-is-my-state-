import pandas as pd
from turtle import Screen
from goto_pos import GoTo

screen = Screen()
screen.bgpic('blank_states_img.gif')
screen.setup(700, 700)

score = 0

states_info = pd.read_csv("50_states.csv")
state = list(states_info['state'])
x = list(states_info['x'])
y = list(states_info['y'])


while True:
    user_answer = screen.textinput(f'score:{score}/50', 'Enter a state:')
    if user_answer.title() in state:
        score += 1
        point = GoTo()
        point.perf(user_answer=user_answer, x=x, y=y, state=state)



#screen.exitonclick()
