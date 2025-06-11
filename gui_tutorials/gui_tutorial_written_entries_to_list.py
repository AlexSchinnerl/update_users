import tkinter as tk
from ttkbootstrap import Style
from tkinter import filedialog


STANDARD_FONT = ("Arial", 18)

root = tk.Tk()
root.title("Update User Roles")
root.geometry("700x500")

style = Style(theme="darkly")

# ----------------------------------------------
# Written entries to List
# ----------------------------------------------

my_entries = []


def something():
    entry_list = ""
    for entries in my_entries:
        entry_list = entry_list + str(entries.get()) + "\n"
        my_label.config(text=entry_list)


for x in range(5):
    my_entry = tk.Entry(root)
    my_entry.grid(row=0, column=x, pady=20, padx=5)
    my_entries.append(my_entry)


my_button = tk.Button(root, text="Click me!", command=something)
my_button.grid(row=1, column=0, pady=20)

my_label = tk.Label(root, text=" ")
my_label.grid(row=2, column=0, pady=20)

root.mainloop()