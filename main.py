# import modules
import requests
import time
import tkinter as tk

# configure the app design
window = tk.Tk()
window.geometry("800x650")
window.title("What is the weather")

t_1 = ("Times", "16", "bold")
t_2 = ("Times", "36", "bold")

searchfield = tk.Entry(window, font=t_1)
searchfield.pack(pady=35)
searchfield.focus()

label_1 = tk.Label(window, font=t_1)
label_1.pack()
label_2 = tk.Label(window, font=t_2)
label_2.pack()

window.mainloop()