import tkinter as tk
# import ttkbootstrap as ttk
import ttkbootstrap as tb
from tkinter import filedialog


STANDARD_FONT = ("Arial", 18)

root = tk.Tk()
root.title("Update User Roles")
root.geometry("700x500")

style = tb.Style(theme="darkly")


# my_label = tk.Label(text="Click Checkbutton", font=STANDARD_FONT)
# my_label.grid(row=0, column=1, pady=(40,10))

# Checkbutton

def checker():
    if var2.get():
        my_label.config(text="Checked")
    else:
        my_label.config(text="Unchecked")

# Toggle Button

# var2 = tk.BooleanVar() # Sorgt für True-False Logik
# my_check2 = tb.Checkbutton(bootstyle="success, round-toggle",
#                            text="Check me!", 
#                            variable= var2,
#                            command=checker # eine Funktion, die beim check ausgeführt wird
#                            )

# my_check2.pack(pady=10)


# multiple Checkbuttons

check_dict = {
    "test1":False,
    "test2":False,
    "test3":False,
    "test4":False,
    "test5":False
}

check_list = []

row_counter = 0
var2 = tk.BooleanVar()

for role in check_dict:
    my_checker = tb.Checkbutton(bootstyle="success, round-toggle",
                                text="Check me!",
                                variable= var2,
                                command=checker
                                )
    my_checker.grid(row=row_counter, column=0, pady=20, padx=5)
    check_list.append(my_checker)
    row_counter += 1





root.mainloop()