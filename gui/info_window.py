import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledText

from utils import getAPIkey, load_roles, modify_roles, update_roles

from .gui_utils import INFOSCREEN_WINDOW_SIZE

class Info_Window(tk.Toplevel):
    # Progress Bar
        # Working on entry 1 of 1000
    # Text from Functions:
        # loaded
        # roles removed
        # user Roles applied
        # output written
        # user AK122837 updated
        # 1 user(s) updated
        # ---------------------------
    def __init__(self, akNumbers, roles_list, work_in_production):
        super().__init__()
        

        self.work_in_production = work_in_production
        self.roles_list = roles_list
        self.akNumbers = akNumbers


        self.title("Infobox")
        # self.iconbitmap()
        self.geometry(INFOSCREEN_WINDOW_SIZE)
        # self.attributes("-fullscreen", True)
        self.style = tb.Style(theme="superhero")
        # self.style = tb.Style(theme="darkly")

        self.percent_bar = tb.Floodgauge(self, bootstyle="success",
                         font=("Arial", 18),
                         mask="Pos: {}",
                         maximum=100,
                         orient="horizontal",
                         mode="determinate",
                         value=0 # Start Value
                         )
        self.percent_bar.pack(pady=20)

        self.infotext = ScrolledText(self, height=20, width=110, wrap=tk.WORD)
        self.infotext.pack(pady=15)











# def increment():
#     my_gauge.step(10)

#     # my_label.config(text=my_prograssbar["value"])




# my_gauge.pack(pady=40, fill=tk.X, padx=20)

# my_button = tb.Button(root, text = "+", bootstyle="info", command=increment)
# my_button.pack(pady=20)

# my_label = tb.Label(root, text="")
# my_label.pack(pady=10)

# # for i in range(50):
# #     my_prograssbar["value"] +=1


# root.mainloop()
