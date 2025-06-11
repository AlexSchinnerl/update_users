import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledText
from tkinter import filedialog

from pathlib import Path

import re

STANDARD_FONT = ("Arial", 14)
TITLE_FONT = ("Arial", 18)

root = tk.Tk()
root.title("Update User Roles")
root.geometry("700x500")

style = tb.Style(theme="darkly")

# Checkbox if work in production
def checker():
    print(work_in_production.get())


work_in_production = tk.BooleanVar()
production_checker = tk.Checkbutton(root, text="Work in Production", variable=work_in_production, command=checker, font=STANDARD_FONT)
production_checker.pack()


# GRID LAYOUT
# -------------------------------------------------------------
# Checkbox if work in production or sandbox
# Select users                          | Ad Roles
# text indput (copy/paste list of AKNr) | Checkboxes of roles
# Apply Button
# -------------------------------------------------------------


# create frame
main_frame = tk.Frame(root)
main_frame.pack(pady=20)

title_label_user = tk.Label(main_frame, text="Select Users", font=TITLE_FONT)
title_label_user.grid(row=0, column=0)

title_label_roles = tk.Label(main_frame, text="Select Role", font=TITLE_FONT)
title_label_roles.grid(row=0, column=1)


# Build checkboxes from role templates in folder

path = Path("roles_xml")
display_roles_list = [file.stem for file in path.rglob("*.xml")]

roles_list = []
rowcount = 1
for role in display_roles_list:
    check = tk.Checkbutton(main_frame, text=f"{role}", variable=role, command=lambda x=role:roles_list.append(x), font=STANDARD_FONT)
    check.grid(row=rowcount, column=1)
    rowcount+=1


# Users Input
# Has to be after Checkboxes tu use rowcount of checkboxes for rowspan
# akNumbers = []
users_text = ScrolledText(main_frame, height=20, width=110, wrap=tk.WORD)
users_text.grid(row=1, column=0, rowspan=rowcount)



# apply Button - in the end: starts program

def apply_function():
    # disable Button
    apply_button["state"] = tk.DISABLED
    apply_infotext.config(text="Änderungen werden durchgeführt...")

    # check users
    text_input = users_text.get(1.0, tk.END)
    akNumbers = re.findall("AK\d{6}", text_input)
    print(akNumbers)
    # check roles
    print(roles_list)


apply_button = tk.Button(root,text="Apply Role Changes",command=apply_function)
apply_button.pack(pady=20)
# print("Apply Btn", roles_list, akNumbers)

# Shows info if Apply is pressed
apply_infotext = tk.Label(root, text="") 
apply_infotext.pack()


root.mainloop()

# https://www.youtube.com/watch?v=aAk3ORDr63U

