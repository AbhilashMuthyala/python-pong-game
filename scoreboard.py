from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score_left = 0
        self.current_score_right = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.board_refresh()

    def board_refresh(self):
        self.clear()
        self.write(f" {self.current_score_left} : {self.current_score_right} ",move=False, align='center',font=('Courier', 20, 'normal'))
    def gameover_board(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game_over - left paddle Score = {self.current_score_left}  right paddle Score = {self.current_score_right} ",move=False, align='center',font=('Courier', 14, 'normal'))
