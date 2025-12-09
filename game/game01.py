from tkinter import *
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)

        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3

        self.canvas_height = canvas.winfo_height()
        self.canvas_width = canvas.winfo_width()

        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        return(
            pos[2] >= paddle_pos[0]
            and pos[0] <= paddle_pos[2]
            and pos[3] >= paddle_pos[1]
            and pos[3] <= paddle_pos[3]
        )
    
    def draw(self):
        if self.hit_bottom:
            return
        
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 3
        
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        
        if self.hit_paddle(pos):
            self.y = -3

        if pos[0] <= 0:
            self.x = 3

        if pos[2] >= self.canvas_width:
            self.x = -3

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)

        self.x = 0
        self.canvas_width = canvas.winfo_width()

        canvas.bind_all('<KeyPress-Left>', self.turn_left)
        canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, evt):
        self.x = -3

    def turn_right(self, evt):
        self.x = 3

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = 0

def restart_game():
    global ball, paddle, game_over_text
    canvas.delete("all")
    paddle = Paddle(canvas, 'blue')
    ball = Ball(canvas, paddle, 'red')
    game_over_text = None

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')
game_over_text = None

restart_btn = Button(tk, text="Restart", command=restart_game)
restart_btn.pack(pady=5)

while True:
    if not ball.hit_bottom:
        ball.draw()
        paddle.draw()

    else:
        if game_over_text is None:
            game_over_text = canvas.create_text(
                250, 200,
                text="GAME OVER",
                font=("Arial", 30),
                fill = "red"
            )
    tk.update()
    time.sleep(0.01)