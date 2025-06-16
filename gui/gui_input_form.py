import tkinter as tk
from ttkbootstrap.scrolled import ScrolledText
from .gui_const import STANDARD_FONT, TITLE_FONT

class Input_Form(tk.Frame):
    def __init__(self, parent): # parent wird die Roles_GUI Klasse werden. Die GUI Klasse wird parent von Frame.
        super().__init__(parent) # weil tk.Frame - der braucht das parent Argument
        # NB! parent ist in diesem Fall ja roles_GUI, was wiederum von tk.Tk erbt und ist daher das gleiche wie root = tk.Tk() und tk.Frame braucht ein root, in diesem Fall die Roles_GUI Klasse

        self.pack(pady=20)

        self.title_label_user = tk.Label(self, text="Select Users", font=TITLE_FONT)
        self.title_label_roles = tk.Label(self, text="Select Role", font=TITLE_FONT)

        self.title_label_user.grid(row=0, column=0, padx=20)
        self.title_label_roles.grid(row=0, column=1, padx=20)

        # Build checkboxes from role templates in folder
        rowcount = 1
        self.checkbuttons_var = []
        for role in parent.display_roles_list:
            var = tk.BooleanVar()
            self.checkbuttons_var.append(var) # creates a list of true/False variables for checkbuttons
            self.check = tk.Checkbutton(self, text=f"{role}", variable=var, font=STANDARD_FONT)
            self.check.grid(row=rowcount, column=1, padx=20)
            rowcount+=1

        # Users Input
        # Has to be after Checkboxes tu use rowcount of checkboxes for rowspan
        self.users_text = ScrolledText(self, height=20, width=100, wrap=tk.WORD)
        self.users_text.grid(row=1, column=0, rowspan=rowcount, padx=20)