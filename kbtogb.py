from tkinter import *
import tkinter as tk
from tkinter import Button, ttk

root = tk.Tk()

root.title("KB to GB")
root.config(height=80,width=250)
root.wm_iconbitmap('')

# Calcularion logic
def calculation():

# Get The infotmation of entry
    kb = kbentry.get()
    mb = int(kb) / 1024 
    gb = mb / 1024

# Prints the calculation in GB
    result = ttk.Label(text=f"There are {gb} GB")
    result.place(x=0, y=40)

kbLabel = ttk.Label(text="KB")
kbLabel.place(x=0, y=10)

# KB input
kbentry = tk.Entry()
kbentry.place(x=30, y=10)

# Button to calculate
calculate = ttk.Button(text="Calculate", command=calculation)
calculate.place(x=170, y=10)

kbLabel = ttk.Label(text="Developed By Lucoberto")
kbLabel.place(x=0, y=60)

root.mainloop()