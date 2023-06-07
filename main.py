import tkinter as tk
import random

win = tk.Tk()

w = 500
h = 500

head = [500//2,500//2]
moving = [0,-1]
whole_snake = []
speed = 100

canvas = tk.Canvas(width = w, height = h, bg = "white")
canvas.pack()


def draw_snake():
    global head
    canvas.create_rectangle(head[0],head[1],head[0]+1,head[1]+1,outline="red",fill="black",width=10)
    head[0] += moving[0]
    head[1] += moving[1]
    canvas.after(speed,draw_snake)

draw_snake()

def changer(e):
    global moving
    global speed
    print("clicked")
    if e.char=="w":
        moving = [0,-1]
    elif e.char == "a":
        moving = [-1,0]
    elif e.char == "d":
        moving = [1,0]
    elif e.char == "s":
        moving = [0,1]
    elif e.char == "k":
        speed -= 10
    elif e.char == "l":
        speed += 10


win.bind("<KeyPress>",changer)

win.mainloop()
