import tkinter as tk
# import ttkbootstrap as ttk
import ttkbootstrap as tb
from tkinter import filedialog


STANDARD_FONT = ("Arial", 18)

root = tk.Tk()
root.title("Update User Roles")
root.geometry("700x500")

style = tb.Style(theme="darkly")

def switch():
    my_button["state"] = tk.DISABLED
    my_label.config(text="Äderungen werden durchgeführt")

my_button = tk.Button(root, text="Click me!", command=switch)
my_button.pack()

my_label = tk.Label(root, text="")
my_label.pack()

root.mainloop()