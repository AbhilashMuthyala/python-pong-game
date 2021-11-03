from turtle import Turtle,Screen
import turtle

class Screen_build():
    def __init__(self):
        self.screen1 = Screen()
        self.screen_build()
        self.screen1.tracer(0)
        self.paddle_list = []

    def screen_update(self):
        self.screen1.update()

    def screen_build(self):
        self.screen1 = Screen()
        self.screen1.bgcolor('black')
        self.screen1.setup(800,600)
        self.screen1.title("Pong Game")

    def exit_on_click(self):
        self.screen1.exitonclick()

    def create_paddle(self,x,y):
        paddle = Turtle(shape='square')
        paddle.penup()
        paddle.speed('fastest')
        paddle.shapesize(stretch_wid=5,stretch_len=1)
        paddle.fillcolor('White')
        paddle.forward(100)
        paddle.setx(x)
        paddle.sety(y)
        self.paddle_list.append(paddle)


    def go_up(self):
        new_y = self.paddle_list[0].ycor() + 20
        self.paddle_list[0].goto(self.paddle_list[0].xcor(),new_y)

    def go_down(self):
        new_y = self.paddle_list[0].ycor() - 20
        self.paddle_list[0].goto(self.paddle_list[0].xcor(), new_y)


    def go_up_1(self):
        new_y = self.paddle_list[1].ycor() + 20
        self.paddle_list[1].goto(self.paddle_list[1].xcor(),new_y)

    def go_down_1(self):
        new_y = self.paddle_list[1].ycor() - 20
        self.paddle_list[1].goto(self.paddle_list[1].xcor(), new_y)

    def move_paddle1(self):
        self.screen1.listen()
        self.screen1.onkeypress(self.go_up,'Up')
        self.screen1.onkeypress(self.go_down, 'Down')
        self.screen1.onkeypress(self.go_up_1,'w')
        self.screen1.onkeypress(self.go_down_1, 's')

    def draw_line(self):
        line = Turtle()
        line.color('white')
        line.speed('fastest')
        line.penup()
        line.goto(0,300)
        line.pendown()
        line.setheading(270)
        line.forward(600)
