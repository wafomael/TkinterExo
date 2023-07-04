from tkinter import *
from random import *

window = Tk()
window.title("PONG")
window.geometry("500x500")
window.minsize(500, 500)
window.config(background="#4D4D4D")

x = 0
y = 5
provenance = 1
le_gagnant = "player"

def starts():
    start.destroy()
    indication.destroy()
    indication2.destroy()
    map.pack(expand=YES)
    balle_move()
    map.after(100, comportement_balle)

def balle_move():
    global x
    global y
    map.move(balle, x, y)
    map.after(100, balle_move)

def comportement_balle():
    global x
    global y
    global provenance
    global le_gagnant
    rdm = [0, 1]
    pl1x1, pl1y1, pl1x2, pl1y2 = map.coords(pl1)
    pl2x1, pl2y1, pl2x2, pl2y2 = map.coords(pl2)
    x1, y1, x2, y2 = map.coords(balle)
    alea = choice(rdm)
    alea_direction1 = choice(range(-3, 0))
    alea_direction2 = choice(range(0, 3))
    if y2 >= pl2y2 - 9 and pl2x1 <= x1 <= pl2x2:
        if alea == 1:
            x = -4 + alea_direction1
            y = -5 + alea_direction1
        elif alea == 0:
            x = 5 + alea_direction1
            y = -5 + alea_direction1
        provenance = 0
    elif y1 <= pl1y1 + 9 and pl1x1 <= x1 <= pl1x2:
        if alea == 1:
            x = 5 - alea_direction2
            y = 5 - alea_direction2
        elif alea == 0:
            x = -4 - alea_direction2
            y = 5 - alea_direction2
        provenance = 1
    if x1 <= 0:
        if provenance == 1:
            x = 6
            y = 4
        elif provenance == 0:
            x = 6
            y = -4
    elif x1 >= largeur - 30:
        if provenance == 1:
            x = -6
            y = 4
        elif provenance == 0:
            x = -6
            y = -4
    if y1 <= pl1y1:
        map.destroy()
        gagnant.pack(expand=YES)

    elif y1 >= pl2y2:
        map.destroy()
        gagnant2.pack(expand=YES)
    map.after(100, comportement_balle)


def move(event):
    if event.keysym == "Left":
        map.move(pl1, -5, 0)
    elif event.keysym == "Right":
        map.move(pl1, 5, 0)
def move2(event):
    if event.keysym == 'q':
        map.move(pl2, -5, 0)
    elif event.keysym == 'd':
        map.move(pl2, 5, 0)

largeur = 300
hauteur = 300
frame = Frame(window, background="#4D4D4D")
map = Canvas(window, width=largeur, height=hauteur, bg="gray", bd=0, highlightthickness=0)

indication = Label(window, text="En bleu le joueur 1 en vert le joueur 2 cliker sur start pour commencer", font=("Cambria Math", 11), bg="#4D4D4D", fg="#DED46E")
indication.pack()
indication2 = Label(window, text="joueur 1 (les fleche). joeur 2 (q et d) ", font=("Cambria Math", 15), bg="#4D4D4D", fg="#DED46E")
indication2.pack()
start = Button(window, text="start", font=("Cambria Math", 20), bg="#DED46E", width=10, command=starts)
start.pack(expand=YES)
gagnant = Label(window, text="le gagnat est le jouer 2", font=("Cambria Math", 20), bg="#4D4D4D", fg="#55C264")
gagnant2 = Label(window, text="le gagnat est le jouer 1", font=("Cambria Math", 20), bg="#4D4D4D", fg="#537BC2")
pl1 = map.create_rectangle(20, 10, 120, 20, fill="#537BC2")
pl2 = map.create_rectangle(230, 290, 120, 280, fill="#55C264")
balle = map.create_oval(100, 100, 70, 70)


map.bind_all('<Left>', move)
map.bind_all('<Right>', move)
map.bind_all('<q>', move2)
map.bind_all('<d>', move2)

window.mainloop()