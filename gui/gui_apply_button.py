import re
import tkinter as tk
from ttkbootstrap.dialogs import Messagebox

from test import run_program

# https://stackoverflow.com/questions/73931962/tkinter-button-class-creation

class Apply_Button(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pack(pady=20)

        self.apply_button = tk.Button(self,text="Apply Role Changes",command=self.apply_function)
        self.apply_infotext = tk.Label(self, text="test")
        
        self.apply_button.grid(row=0, column=0)
        self.apply_infotext.grid(row=0, column=1, padx=20)

        self.parent = parent
    
    def apply_function(self):
        # print(type(self.parent))

        self.process_input()

        # Zusammenfassung was durchgeführt wird.
        message_string = str(
            f"Folgende Änderungen werden durchgeführt:\n"+
            f"Rollen: {self.parent.roles_list}\n"+
            f"Angewendet auf {self.parent.akNumbers}\n"+
            f"Änderungen werden durchgeführt in: {'Produktivsystem' if self.parent.work_in_production.get() else 'Sandbox'}"
        )
        if Messagebox.okcancel(
            title="Zusammenfassung",
            message=message_string
            # message=f"Folgende Änderungen werden durchgeführt:\nRollen: {self.roles_list}\n angewendet auf {self.akNumbers}"
            ) == "OK":

            if self.parent.work_in_production.get():
                if Messagebox.okcancel(title="Achtung!", message="Änderungen im Produktivsystem - Bitte nochmal bestätigen!") == "OK":
                    self.apply_button_disable()
                    run_program(self.parent, self.parent.akNumbers, self.parent.roles_list, self.parent.work_in_production.get())
                else:
                    self.clear_input()
            else:
                self.apply_button_disable()
                run_program(self.parent, self.parent.akNumbers, self.parent.roles_list, self.parent.work_in_production.get())
        else:
            self.clear_input()       

    def apply_button_disable(self):
        # disable Button
        self.apply_button.config(state = tk.DISABLED) # um sicherzustellen, dass der Button nur einmal gedrückt wird.
        self.apply_infotext.config(text="Änderungen werden durchgeführt...")
    
    def process_input(self):
        # Process input (AKNrs and Roles List)
        self.parent.akNumbers = re.findall("AK\d{6}", self.parent.input_form.users_text.get(1.0, tk.END))
        for num, var in enumerate(self.parent.input_form.checkbuttons_var):
            # translates the true/false list in roles
            if var.get():
                self.parent.roles_list.append(self.parent.display_roles_list[num])# = [var.get() for var in self.input_form.checkbuttons_var]
    
    def clear_input(self):
        self.parent.akNumbers = []
        self.parent.roles_list = []