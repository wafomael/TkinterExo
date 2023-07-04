import tkinter as tk

# Définir la couleur initiale
color = "blue"

def change_color_to_red():
    global color
    color = "red"

def change_color_to_blue():
    global color
    color = "blue"

def create_square(x, y):
    canvas.create_rectangle(x, y, x+50, y+50, fill=color)

root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

circle = canvas.create_oval(140, 140, 160, 160, fill="yellow")

red_button = tk.Button(root, text="Red", command=change_color_to_red)
red_button.pack()

blue_button = tk.Button(root, text="Blue", command=change_color_to_blue)
blue_button.pack()

root.bind("<Up>", lambda e: create_square(150, 140))

root.mainloop()
