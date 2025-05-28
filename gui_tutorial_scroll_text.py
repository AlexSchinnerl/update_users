import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledText

STANDARD_FONT = ("Arial", 18)

root = tk.Tk()
root.title("Update User Roles")
root.geometry("700x500")

style = tb.Style(theme="darkly")

# Text

my_text = ScrolledText(root, height=20, width=110, wrap=tk.WORD)
my_text.pack(pady=15)


def get_text():
    my_label.config(text=my_text.get("start", tk.END))

get_text_button = tk.Button(root, text="Get Text", command=get_text)
get_text_button.pack()

my_label = tk.Label(root, pady=20)
my_label.pack()


root.mainloop()