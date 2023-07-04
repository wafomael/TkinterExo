from tkinter import *

couleur = "#000000"
def choix_color0():
    global couleur
    couleur = "#000000"
def choix_color1():
    global couleur
    couleur = "#FFFFFF"
def choix_color2():
    global couleur
    couleur = "#FF0000"
def choix_color3():
    global couleur
    couleur = "#FF8A00"
def choix_color4():
    global couleur
    couleur = "#FFE900"
def choix_color5():
    global couleur
    couleur = "#0DFF00"
def choix_color6():
    global couleur
    couleur = "#00AAFF"
def choix_color7():
    global couleur
    couleur = "#0900FF"
def choix_color8():
    global couleur
    couleur = "#8700FF"
def choix_color9():
    global couleur
    couleur = "#FF00FA"
def choix_color10():
    global couleur
    couleur = "#7D5959"
def choix_color11():
    global couleur
    couleur = "#808080"

def stop_dessin():
    global activation
    if activation == 'O':
        activation = 'N'
        bouton_dessin.config(state=NORMAL)

def effacer():
    x1, y1, x2, y2 = map.coords(cursseur)
    map.create_rectangle(x1,y1, x2, y2, fill="#FFFFFF", outline="")

def clear():
    global map
    map.destroy()
    largeur = 600
    hauteur = 400
    map = Canvas(window, bg="#FFFFFF", width=largeur, height=hauteur, bd=0, highlightthickness=0)
    cursseur = map.create_oval(0, 0, 20, 20, fill="#FFFFFF")
    map.pack(expand=YES)

def move(event):
    global couleur
    if event.keysym == 'Up':
        map.move(cursseur, 0, -20)
    elif event.keysym == 'Down':
        map.move(cursseur, 0, 20)
    elif event.keysym == 'Left':
        map.move(cursseur, -20, 0)
    elif event.keysym == 'Right':
        map.move(cursseur, 20, 0)
    if activation == 'O':
        x1, y1, x2, y2 = map.coords(cursseur)
        map.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="")

activation = 'N'
def draw_statut():
    global activation
    if activation != 'O':
        activation = 'O'
        bouton_dessin.config(state=DISABLED)




touches = [
    {'couleur': '#000000', 'row': 0, 'colunm': 0, 'comande': choix_color0},
    {'couleur': '#FFFFFF', 'row': 0, 'colunm': 1, 'comande': choix_color1},
    {'couleur': '#FF0000', 'row': 0, 'colunm': 2, 'comande': choix_color2},
    {'couleur': '#FF8A00', 'row': 0, 'colunm': 3, 'comande': choix_color3},
    {'couleur': '#FFE900', 'row': 0, 'colunm': 4, 'comande': choix_color4},
    {'couleur': '#0DFF00', 'row': 0, 'colunm': 5, 'comande': choix_color5},
    {'couleur': '#00AAFF', 'row': 1, 'colunm': 0, 'comande': choix_color6},
    {'couleur': '#0900FF', 'row': 1, 'colunm': 1, 'comande': choix_color7},
    {'couleur': '#8700FF', 'row': 1, 'colunm': 2, 'comande': choix_color8},
    {'couleur': '#FF00FA', 'row': 1, 'colunm': 3, 'comande': choix_color9},
    {'couleur': '#7D5959', 'row': 1, 'colunm': 4, 'comande': choix_color10},
    {'couleur': '#808080', 'row': 1, 'colunm': 5, 'comande': choix_color11},
]

window = Tk()

window.title("Fake Paint")
window.geometry("700x500")
window.minsize(700, 500)
window.config(background="#B8B8B8")

frame = Frame(window, background="#B8B8B8")
largeur = 600
hauteur = 400
map = Canvas(window, bg="#FFFFFF", width=largeur, height=hauteur, bd=0, highlightthickness=0)

for indc_touche in touches:
    touche = Button(frame, bg=indc_touche['couleur'], command=indc_touche['comande'])
    touche.grid(row=indc_touche['row'], column=indc_touche['colunm'])

bouton_dessin = Button(frame, bg="#808080", text="crayon ", fg="#FFFFFF", command=draw_statut)
bouton_dessin.grid(row=0, column=6)

bouton_effacer = Button(frame, bg="#FFBBBB", text="gomme", command=effacer)
bouton_effacer.grid(row=1, column=6)

bouton_dessin_off = Button(frame, bg="#C4C4C4", text="  stop dessin", command=stop_dessin)
bouton_dessin_off.grid(row=0, column=7)

bouton_clear = Button(frame, bg="#D96969", text=" Tout Effacer", command=clear)
bouton_clear.grid(row=1, column=7)

bouton_save = Button(frame, bg="#A59AE3", text=" sauvgarder")
bouton_save.grid(row=0, column=8, rowspan=2)

cursseur = map.create_oval(0, 0, 20, 20, fill="#FFFFFF")

frame.pack()
map.pack(expand=YES)

map.bind_all('<Up>', move)
map.bind_all('<Down>', move)
map.bind_all('<Left>', move)
map.bind_all('<Right>', move)

window.mainloop()