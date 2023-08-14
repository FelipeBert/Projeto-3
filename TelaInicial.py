from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1920x1080")
window.configure(bg = "#FFFFFF")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"images/background.png")
background = canvas.create_image(
    960.0, 540.0,
    image=background_img)

canvas.create_text(
    1800.0, 259.0,
    text = "Conecte ao Facebook",
    fill = "#ffffff",
    font = ("Cabin-Bold", int(15.0)))

canvas.create_text(
    173.5, 553.5,
    text = "Em Breve\n",
    fill = "#ffffff",
    font = ("Cabin-Bold", int(22.0)))

canvas.create_text(
    186.0, 63.0,
    text = "Comunidade\n",
    fill = "#ffffff",
    font = ("Cabin-Bold", int(22.0)))

img0 = PhotoImage(file = f"images/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 30, y = 175,
    width = 27,
    height = 27)

img1 = PhotoImage(file = f"images/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 30, y = 1024,
    width = 27,
    height = 27)

img2 = PhotoImage(file = f"images/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 29, y = 97,
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
    x = 29, y = 22,
    width = 28,
    height = 28)

img4 = PhotoImage(file = f"images/img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 116, y = 101,
    width = 323,
    height = 211)

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

window.resizable(False, False)
window.mainloop()
