import tkinter as tk
# import ttkbootstrap as ttk
from ttkbootstrap import Style
from tkinter import filedialog


STANDARD_FONT = ("Arial", 18)

root = tk.Tk()
root.title("Update User Roles")
root.geometry("700x500")

style = Style(theme="darkly")

# create frame
my_frame = tk.Frame(root)
my_frame.pack(pady=20)

title_label_user = tk.Label(my_frame, text="Select User", font=STANDARD_FONT)
title_label_user.grid(row=0, column=0)

title_label_roles = tk.Label(my_frame, text="Select Role", font=STANDARD_FONT)
title_label_roles.grid(row=0, column=1)


check_state = tk.IntVar() # eine Variable muss den state (True/False) der checkbox speichern
check = tk.Checkbutton(my_frame, text="User Role Dummy", font=STANDARD_FONT, variable=check_state)
check.grid(row=1, column=1)#, sticky=tk.W+tk.E)

root.mainloop()