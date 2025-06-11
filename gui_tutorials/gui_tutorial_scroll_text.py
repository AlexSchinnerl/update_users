import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledText

import re

STANDARD_FONT = ("Arial", 18)

root = tk.Tk()
root.title("Update User Roles")
root.geometry("700x500")

style = tb.Style(theme="darkly")

# Text

my_text = ScrolledText(root, height=20, width=110, wrap=tk.WORD)
my_text.pack(pady=15)


def get_text():
    work_text = my_text.get(1.0, tk.END)
    akNumbers = re.findall("AK\d{6}", work_text)
    print(akNumbers)
    for akNumber in akNumbers:
        print(f"AKNR: {akNumber}")

get_text_button = tk.Button(root, text="Get Text", command=get_text)
get_text_button.pack()

my_label = tk.Label(root, pady=20)
my_label.pack()


root.mainloop()