from turtle import Turtle


class GoTo(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def perf(self, user_answer, x, y, state):
        i = state.index(user_answer.title())
        self.goto(x[i], y[i])
        self.write(user_answer)


