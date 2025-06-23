import re
import tkinter as tk

from .gui_utils import confirmation_message
from test import run_program

# https://stackoverflow.com/questions/73931962/tkinter-button-class-creation

class Apply_Button(tk.Frame):
    def __init__(self, parent, input_form):
        super().__init__(parent)

        self.pack(pady=20)

        self.apply_button = tk.Button(self,text="Apply Role Changes",command=self.apply_function)
        self.apply_infotext = tk.Label(self, text="test")
        
        self.apply_button.grid(row=0, column=0)
        self.apply_infotext.grid(row=0, column=1, padx=20)

        self.parent = parent
        self.input_form = input_form
    
    def apply_function(self):
        # Process input (AKNrs and Roles List)
        # self.parent.akNumbers = re.findall("AK\d{6}", self.parent.input_form.users_text.get(1.0, tk.END))
        self.parent.akNumbers = re.findall("AK\d{6}", self.input_form.users_text.get(1.0, tk.END))
        for num, var in enumerate(self.input_form.checkbuttons_var):
            # translates the true/false list in roles
            if var.get():
                self.parent.roles_list.append(self.parent.display_roles_list[num])# = [var.get() for var in self.input_form.checkbuttons_var]

        if confirmation_message(self.parent):
            self.apply_button.config(state = tk.DISABLED) # um sicherzustellen, dass der Button nur einmal gedrückt wird.
            self.apply_infotext.config(text="Änderungen werden durchgeführt...")
            run_program(self.parent)
        else:
            # clear input
            self.parent.akNumbers = []
            self.parent.roles_list = []