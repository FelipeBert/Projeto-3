from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1920x1080")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"images/background3.png")
background = canvas.create_image(
    935.5, 530.5,
    image=background_img)

img0 = PhotoImage(file = f"images/img16.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 105, y = 5,
    width = 267,
    height = 101)

img1 = PhotoImage(file = f"images/img17.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 32, y = 991,
    width = 27,
    height = 27)

img2 = PhotoImage(file = f"images/img18.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 22, y = 183,
    width = 38,
    height = 39)

img3 = PhotoImage(file = f"images/img19.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 32, y = 106,
    width = 28,
    height = 28)

img4 = PhotoImage(file = f"images/img20.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 32, y = 28,
    width = 28,
    height = 28)

canvas.create_text(
    1641.5, 998.0,
    text = "Contagem: 0",
    fill = "#ffffff",
    font = ("Cabin-Regular", int(64.0)))

canvas.create_text(
    338.0, 1001.0,
    text = "Status: falso",
    fill = "#ffffff",
    font = ("Cabin-Regular", int(64.0)))

canvas.create_text(
    977.5, 66.0,
    text = "Atividade: Flexão",
    fill = "#ffffff",
    font = ("Cabin-Regular", int(64.0)))

window.resizable(False, False)
window.mainloop()
