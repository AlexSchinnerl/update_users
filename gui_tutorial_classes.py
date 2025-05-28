import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from ttkbootstrap import Style

STANDARD_FONT = ("Arial", 18)

# https://www.youtube.com/watch?v=ibf5cx221hk

# best Practice - arbeiten mit Klassen
class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.style = Style(theme="darkly")

        self.label = tk.Label(self.root, text="Your Label", font=STANDARD_FONT)
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=STANDARD_FONT)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar() # eine Variable muss den state (True/False) der checkbox speichern
        self.check = tk.Checkbutton(self.root, text="Show Message Box", font=STANDARD_FONT, variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=STANDARD_FONT, command=self.show_message)
        self.button.pack(padx=10, pady=10)


        self.root.mainloop()
    
    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get("1.0", tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get("1.0", tk.END))


MyGUI()