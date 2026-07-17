from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")
GAME_OVER_FONT = ("Arial", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(
            f"GAME OVER\n\nFinal Score: {self.score}\n\nPress Y to Play Again\nPress N to Exit",
            align=ALIGNMENT,
            font=GAME_OVER_FONT,
        )

    def reset(self):
        self.score = 0
        self.update_scoreboard()