import tkinter as tk
from pathlib import Path

root = tk.Tk()    

path = Path("roles_xml")
roles_list = [file.stem for file in path.rglob("*.xml")]

selected_roles = []
for role in roles_list:
    check = tk.Checkbutton(root, text=f"{role}", variable=role, command=lambda x=role:selected_roles.append(x))
    check.pack(anchor="w")

tk.Button(root,text="Ok",command=lambda: [print(selected_roles),root.destroy()]).pack()

root.mainloop()



