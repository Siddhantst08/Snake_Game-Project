from turtle import Turtle
import winsound
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')
FONT2 = ('Arial', 36, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 350)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"SCORE: {self.score} ", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER !!", False, align=ALIGNMENT, font=FONT2)
        winsound.PlaySound('game_over.wav', winsound.SND_FILENAME)

    def inc_score(self):
        self.score += 1
        self.clear()
        self.update_score()



