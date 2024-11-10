import time

FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-280,270)
        self.display_score()
    def display_score(self):
        self.score+=1
        self.clear()
        self.write(f"LEVEL: {self.score}",align="left",font=FONT)
    def game_over(self):
        self.color("white")
        self.home()
        self.write("GAME OVER", align="center", font=FONT)
