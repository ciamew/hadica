import tkinter as tk

win = tk.Tk()

w = 500
h = 500

head = [500//2,500//2]
moving = [0,-1]
whole_snake = []
speed = 100 #og speed
snake_coordinates = []

canvas = tk.Canvas(width = w, height = h, bg = "black")
canvas.pack()

def draw_snake():
    global head
    canvas.create_rectangle(head[0],head[1],head[0]+1,head[1]+1,outline="white",fill="black",width=3)
    snake_coordinates.append(tuple(head)) #vopcha suradnice hada do snake_coordinates
    if snake_coordinates.count(tuple(head)) > 1: #ak sa dana suradnica vyskitne viac ako 1x konci hra
        canvas.delete("all")
        canvas.create_text(w//2, 400, text="YOU LOST!", font="Arial 15", fill="red")
        return
    head[0] += moving[0]
    head[1] += moving[1]
    canvas.after(speed,draw_snake)
    print(snake_coordinates)
draw_snake()

def changer(e):
    global moving, speed
    print("clicked")
    if e.char == "w": #up
        moving = [0,-1]
    elif e.char == "a": #left
        moving = [-1,0]
    elif e.char == "d": #right
        moving = [1,0]
    elif e.char == "s": #down
        moving = [0,1]
    elif e.char == "k": #makes the snake go faster
        speed -= 10
    elif e.char == "l": #makes the snake go slower
        speed += 10

win.bind("<KeyPress>",changer)

win.mainloop()
