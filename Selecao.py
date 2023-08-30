import tkinter as tk
from tkinter import *
import subprocess
import threading

def init(window):
    for widget in window.winfo_children():
        widget.destroy()

    width= window.winfo_screenwidth()  
    height= window.winfo_screenheight() 
    window.geometry("%dx%d" % (width, height)) 
    window.title("Shape Motion")
    window.iconbitmap("images/ShapeMotion.ico")

    background2_img = PhotoImage(file = f"images/background2.png")
    label_background2 = Label(window, image=background2_img).pack()

    textSelecExer = tk.Label(
        window,
        font=("Cabin-Bold", int(25.0)),
        text="Selecine seu exercicio:",
        background="#1c1c1c",
        foreground="#ffffff"
        )
    textSelecExer.place(x=96,y=50)

    img0 = PhotoImage(file = f"images/img9.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked_home,
        relief = "flat")

    b0.place(
        x = 20, y = 20,
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
        x = 19, y = 103,
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
        x = 20, y = 184,
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
        x = 7, y = 670,
        width=45,
        height=30)

    img4 = PhotoImage(file = f"images/img13.png")
    b4 = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked_img13,
        relief = "flat")

    b4.place(
        x = 500, y = 184,
        width = 300,
        height = 200)

    img5 = PhotoImage(file = f"images/img14.png")
    b5 = Button(
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked_img14,
        relief = "flat")

    b5.place(
        x = 114, y = 184,
        width = 300,
        height = 200)

    img6 = PhotoImage(file = f"images/img15.png")
    b6 = Button(
        image = img6,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked_img15,
        relief = "flat")

    b6.place(
        x = 886, y = 184,
        width = 300,
        height = 200)

    img7 = PhotoImage(file = f"images/img7.png")
    b7 = Button(
        image = img7,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked_img7,
        relief = "flat")

    b7.place(
        x = 114, y = 394,
        width = 300,
        height = 200)

    img8 = PhotoImage(file = f"images/img8.png")
    b8 = Button(
        image = img8,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked_img8,
        relief = "flat")

    b8.place(
        x = 500, y = 394,
        width = 300,
        height = 200)

    botoes = [b0, b1, b2, b3, b4, b5, b6, b7, b8]

    for botao in botoes:
        botao.bind("<Enter>", destacar_botao)
        botao.bind("<Leave>", remover_destaque_botao)

    #window.resizable(False, False)
    window.mainloop()

    
def btn_clicked():
    print("Botão Clicado")

def btn_clicked_home():
    def run_script():
        subprocess.call(["python", "TelaInicial.py"])

    thread = threading.Thread(target=run_script)
    thread.start()

    window.destroy()

def btn_clicked_img15():
    def run_script():
        exercise_type = "push-up"
        root_value = "root_value"
        subprocess.call(["python", "main.py", exercise_type, root_value])

    thread = threading.Thread(target=run_script)
    thread.start()

    window.destroy()

def btn_clicked_img14():
    def run_script():
        exercise_type = "sit-up"
        root_value = "root_value"
        subprocess.call(["python", "main.py", exercise_type, root_value])

    thread = threading.Thread(target=run_script)
    thread.start()

    window.destroy()

def btn_clicked_img13():
    def run_script():
        exercise_type = "squat"
        root_value = "root_value"
        subprocess.call(["python", "main.py", exercise_type, root_value])

    thread = threading.Thread(target=run_script)
    thread.start()

    window.destroy()

def btn_clicked_img7():
    def run_script():
        exercise_type = "walk"
        root_value = "root_value"
        subprocess.call(["python", "main.py", exercise_type, root_value])

    thread = threading.Thread(target=run_script)
    thread.start()

    window.destroy()

def btn_clicked_img8():
    def run_script():
        exercise_type = "pull-up"
        root_value = "root_value"
        subprocess.call(["python", "main.py", exercise_type, root_value])

    thread = threading.Thread(target=run_script)
    thread.start()

    window.destroy()

def destacar_botao(event):
    event.widget.config(bg="gray", cursor="hand2")

def remover_destaque_botao(event):
    event.widget.config(bg="SystemButtonFace", cursor="arrow")