import tkinter as tk 
window=tk.Tk() 
width= window.winfo_screenwidth()  
height= window.winfo_screenheight() 
window.geometry("%dx%d" % (width, height)) 
window.title("Geeeks For Geeks") 
label = tk.Label(window, font="Cabin",text="Em Breve") 
#label.pack() 
label.place(x=163.0,y=415.0)
window.mainloop() 


#canvas.create_text(
#    1800.0, 259.0,
 #   text = "Conecte ao Facebook",
  #  fill = "#ffffff",
   # font = ("Cabin-Bold", int(15.0)))

#canvas.create_text(
#    163.0, 415.0,
 #   text = "Em Breve\n",
  #  fill = "#ffffff",
   # font = ("Cabin-Bold", int(22.0)))

#canvas.create_text(
#    186.0, 63.0,
 #   text = "Comunidade\n",
  #  fill = "#ffffff",
   # font = ("Cabin-Bold", int(22.0)))