from game_screen import Screen_build
from ball import Ball
import time
from scoreboard import Scoreboard

def game_start():
    screen = Screen_build()
    screen.create_paddle(380,0)
    screen.create_paddle(-390,0)
    ball = Ball()
    screen.draw_line()
    screen.move_paddle1()
    scoreboard = Scoreboard()

    game_is_on = True
    while game_is_on:
        time.sleep(ball.val)
        screen.screen_update()
        ball.move()
        ball.detect_collision_wall()
        if (ball.distance(screen.paddle_list[0]) < 40 and ball.xcor() > 370) or (ball.distance(screen.paddle_list[1]) < 40 and ball.xcor() < -370):
            ball.bounce_x()

        if ball.xcor() > 380:
            scoreboard.current_score_left += 1
            scoreboard.board_refresh()
            ball.restart()
        if ball.xcor() < -380:
            scoreboard.current_score_right += 1
            scoreboard.board_refresh()
            ball.restart()

        if scoreboard.current_score_left > 2 or scoreboard.current_score_right > 2:
            print("game over")
            scoreboard.gameover_board()
            game_is_on = False

    screen.exit_on_click()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game_start()


