from tkinter import *

def touche0():
    affichage.insert(END, '0')
def touche1():
    affichage.insert(END, '1')
def touche2():
    affichage.insert(END, '2')
def touche3():
    affichage.insert(END, '3')
def touche4():
    affichage.insert(END, '4')
def touche5():
    affichage.insert(END, '5')
def touche6():
    affichage.insert(END, '6')
def touche7():
    affichage.insert(END, '7')
def touche8():
    affichage.insert(END, '8')
def touche9():
    affichage.insert(END, '9')

toucher = 1

def touche_pls():
    global toucher
    opperation = affichage.get()
    chr_opperation = opperation.split('+')
    if toucher <= 1:
        if '+' not in opperation:
            affichage.insert(END, '+')
            toucher += 1
    if '+' in opperation:
        resultat = float(chr_opperation[0]) + float(chr_opperation[1])
        affichage.delete(0, END)
        affichage.insert(0, str(resultat))
        toucher -= 1

def touche_moins():
    global toucher
    opperation = affichage.get()
    chr_opperation = opperation.split('-')
    if toucher <= 1:
        if '-' not in opperation:
            affichage.insert(END, '-')
            toucher += 1
    if '-' in opperation:
        resultat = float(chr_opperation[0]) - float(chr_opperation[1])
        affichage.delete(0, END)
        affichage.insert(0, str(resultat))
        toucher -= 1

def touche_fois():
    global toucher
    opperation = affichage.get()
    chr_opperation = opperation.split('*')
    if toucher <= 1:
        if '*' not in opperation:
            affichage.insert(END, '*')
            toucher += 1
    if '*' in opperation:
        resultat = float(chr_opperation[0]) * float(chr_opperation[1])
        affichage.delete(0, END)
        affichage.insert(0, str(resultat))
        toucher -= 1

def touche_div():
    global toucher
    opperation = affichage.get()
    chr_opperation = opperation.split('/')
    if toucher <= 1:
        if '/' not in opperation:
            affichage.insert(END, '/')
            toucher += 1
    if '/' in opperation:
        resultat = float(chr_opperation[0]) / float(chr_opperation[1])
        affichage.delete(0, END)
        affichage.insert(0, str(resultat))
        toucher -= 1

def touche_clear():
    global toucher
    affichage.delete(0, END)
    toucher = 1

def touche_egal():
    global toucher
    if '+' in affichage.get():
        operation = affichage.get().split('+')
        resultat = float(operation[0]) + float(operation[1])
        affichage.delete(0, END)
        affichage.insert(0, str(resultat))
    if '-' in affichage.get():
        operation = affichage.get().split('-')
        resultat = float(operation[0]) - float(operation[1])
        affichage.delete(0, END)
        affichage.insert(0, str(resultat))
    if '*' in affichage.get():
        operation = affichage.get().split('*')
        resultat = float(operation[0]) * float(operation[1])
        affichage.delete(0, END)
        affichage.insert(0, str(resultat))
    if '/' in affichage.get():
        operation = affichage.get().split('/')
        resultat = float(operation[0]) / float(operation[1])
        affichage.delete(0, END)
        affichage.insert(0, str(resultat))
    toucher = 1

boutons = [
    {'text': '0 ', 'commande': touche0, 'row': 0, 'colum': 0, 'couleur': '#FFFFFF'},
    {'text': '1 ', 'commande': touche1, 'row': 0, 'colum': 1, 'couleur': '#FFFFFF'},
    {'text': '2 ', 'commande': touche2, 'row': 0, 'colum': 2, 'couleur': '#FFFFFF'},
    {'text': '+', 'commande': touche_pls, 'row': 0, 'colum': 3, 'couleur': '#9BD6D5'},
    {'text': '3 ', 'commande': touche3, 'row': 1, 'colum': 0, 'couleur': '#FFFFFF'},
    {'text': '4 ', 'commande': touche4, 'row': 1, 'colum': 1, 'couleur': '#FFFFFF'},
    {'text': '5 ', 'commande': touche5, 'row': 1, 'colum': 2, 'couleur': '#FFFFFF'},
    {'text': '- ', 'commande': touche_moins, 'row': 1, 'colum': 3, 'couleur': '#9BD6D5'},
    {'text': '6 ', 'commande': touche6, 'row': 2, 'colum': 0, 'couleur': '#FFFFFF'},
    {'text': '7 ', 'commande': touche7, 'row': 2, 'colum': 1, 'couleur': '#FFFFFF'},
    {'text': '8 ', 'commande': touche8, 'row': 2, 'colum': 2, 'couleur': '#FFFFFF'},
    {'text': '* ', 'commande': touche_fois, 'row': 2, 'colum': 3, 'couleur': '#9BD6D5'},
    {'text': '9 ', 'commande': touche9, 'row': 3, 'colum': 0, 'couleur': '#FFFFFF'},
    {'text': 'clr', 'commande': touche_clear, 'row': 3, 'colum': 1, 'couleur': '#8F82D6'},
    {'text': '= ', 'commande': touche_egal, 'row': 3, 'colum': 2, 'couleur': '#8F82D6'},
    {'text': '/ ', 'commande': touche_div, 'row': 3, 'colum': 3, 'couleur': '#9BD6D5'},
]

window = Tk()
window.geometry("240x310")
window.minsize(240, 310)
window.title("CALCULETTE")
window.config(background="#808080")

frame = Frame(window, bg="#808080")

affichage = Entry(window, font=("Cascodia Code", 25), bg="#666666", width=12)
affichage.pack()

for idc_bouton in boutons:
    bouton = Button(frame, font=("Cascodia Code", 25), text=idc_bouton['text'], command=idc_bouton['commande'], bg=idc_bouton['couleur'])
    bouton.grid(row=idc_bouton['row'], column=idc_bouton['colum'])

frame.pack()
window.mainloop()