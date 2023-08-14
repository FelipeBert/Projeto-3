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

background_img = PhotoImage(file = f"images/background2.png")
background = canvas.create_image(
    973.5, 621.0,
    image=background_img)

canvas.create_text(
    616.0, 97.0,
    text = "Selecione o Exercício desejado:",
    fill = "#ffffff",
    font = ("Cabin-Bold", int(40.0)))

img0 = PhotoImage(file = f"images/img9.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 31, y = 20,
    width = 28,
    height = 28)

img1 = PhotoImage(file = f"images/img10.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 31, y = 103,
    width = 28,
    height = 28)

img2 = PhotoImage(file = f"images/img11.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 32, y = 184,
    width = 27,
    height = 27)

img3 = PhotoImage(file = f"images/img12.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 31, y = 1011,
    width = 27,
    height = 27)

img4 = PhotoImage(file = f"images/img13.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 711, y = 193,
    width = 586,
    height = 377)

img5 = PhotoImage(file = f"images/img14.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b5.place(
    x = 114, y = 184,
    width = 592,
    height = 386)

img6 = PhotoImage(file = f"images/img15.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b6.place(
    x = 1294, y = 192,
    width = 594,
    height = 378)

img7 = PhotoImage(file = f"images/img7.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b7.place(
    x = 115, y = 585,
    width = 596,
    height = 381)

img8 = PhotoImage(file = f"images/img8.png")
b8 = Button(
    image = img8,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b8.place(
    x = 710, y = 583,
    width = 591,
    height = 387)

window.resizable(False, False)
window.mainloop()
