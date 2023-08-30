import tkinter as tk
from tkinter import *
import Selecao

window = tk.Tk()
width= window.winfo_screenwidth()  
height= window.winfo_screenheight() 
window.geometry("%dx%d" % (width, height)) 
window.title("Shape Motion")
window.iconbitmap("images/ShapeMotion.ico")

def btn_clicked():
    print("Botão Clicado")

def btn_clicked_img4():
    Selecao.init(window)

def destacar_botao(event):
    event.widget.config(bg="gray", cursor="hand2")

def remover_destaque_botao(event):
    event.widget.config(bg="SystemButtonFace", cursor="arrow")

background_img = PhotoImage(file = f"images/background.png")
label_background = Label(window, image=background_img).pack()

textUpChallenger = tk.Label(
    window,
    font=("Cabin-Bold", int(18.0)),
    text="Em Breve",
    background="#1c1c1c",
    foreground="#ffffff"
    )
textUpChallenger.place(x=96,y=350)

textCommunity = tk.Label(
    window,
    font=("Cabin-Bold", int(18.0)),
    text="Comunidade",
    background="#1c1c1c",
    foreground="#ffffff"
    )
textCommunity.place(x=96,y=50)

img0 = PhotoImage(file = f"images/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 20, y = 175,
    width = 28.5,
    height = 27)

img1 = PhotoImage(file = f"images/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 7, y = 670,
    width=45,
    height=30
    )

img2 = PhotoImage(file = f"images/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 19, y = 97,
    width = 28,
    height = 28)

img3 = PhotoImage(file = f"images/img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 20, y = 22,
    width = 28,
    height = 28)

img4 = PhotoImage(file = f"images/img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked_img4,
    relief = "flat")

b4.place(
    x = 67,
    y = 96,
    width=300,
    height=200
)

img5 = PhotoImage(file = f"images/img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b5.place(
    x = 1754, y = 103,
    width = 86,
    height = 86)

img6 = PhotoImage(file = f"images/img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b6.place(
    x = 1773, y = 733,
    width = 55,
    height = 39)

botoes = [b0, b1, b2, b3, b4, b5, b6]

for botao in botoes:
    botao.bind("<Enter>", destacar_botao)
    botao.bind("<Leave>", remover_destaque_botao)

window.mainloop()
