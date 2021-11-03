from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        #ball = Turtle()
        self.shape('circle')
        self.color('white')
        self.setx(0)
        self.sety(0)
        self.penup()
        self.speed('slowest')
        self.x_move = 10
        self.y_move = 10
        self.val = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def detect_collision_wall(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.bounce_y()

    def bounce_y(self):
        self.y_move *= -1
        self.move()

    def bounce_x(self):
        self.x_move *= -1
        self.move()

    def restart(self):
        self.goto(0,0)
        self.bounce_x()
        self.val = 0.1

    def speed_increase(self):
        self.val *= 0.9









