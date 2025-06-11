import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledText
from ttkbootstrap.dialogs import Messagebox
from pathlib import Path

import re
import os

# https://www.youtube.com/watch?v=X5yyKZpZ4vU
# https://www.youtube.com/watch?v=aAk3ORDr63U

# Wenn die Function nur für Frame relevant, dann in der Frame Klasse anlegen. Wenn relevant für die ganze App, dann in der Main_App

STANDARD_FONT = ("Arial", 14)
TITLE_FONT = ("Arial", 18)

# Class that creates the most basic app

class Roles_GUI(tk.Tk):
    def __init__(self):
        super().__init__() # super().__init__() run constructor of tk.Tk (gleich wie root=tkTk()) D.h. die Klasse gibt uns schon eine Instanz von Tk
        # Das erlaubt uns z.b. self.title zu schreiben anstatt zuerst root = tk.TK().
        # hier braucht man nichts, weil GUI die Parent App ist - In der Child Klasse kommt hier der Parent rein.

        # Title, icon, size
        self.title("Update User Roles")
        # self.iconbitmap()
        self.geometry("1250x750")
        # self.attributes("-fullscreen", True)

        self.style = tb.Style(theme="darkly")

        # Checkbox if work in production
        self.work_in_production = tk.BooleanVar()
        self.production_checker = tk.Checkbutton(self, text="Work in Production", variable=self.work_in_production, font=STANDARD_FONT)
        self.production_checker.pack(pady=20)

        # Create a frame outside of function
        path = Path("roles_xml")
        self.display_roles_list = [file.stem for file in path.rglob("*.xml")]
        self.input_form = Input_Form(self)

        # apply Button - in the end: starts program
        self.apply_button = tk.Button(self,text="Apply Role Changes",command=self.apply_function)
        self.apply_button.pack(pady=20)

        # Shows info if Apply is pressed
        self.apply_infotext = tk.Label(self, text="") 
        self.apply_infotext.pack(pady=20)

        # AK Nums to fill later
        self.akNumbers = []
        self.roles_list = []

    def apply_function(self):

        self.process_input()

        # Zusammenfassung was durchgeführt wird.
        if Messagebox.okcancel(
            title="Zusammenfassung",
            message=f"Folgende Änderungen werden durchgeführt:\nRollen: {self.roles_list}\n angewendet auf {self.akNumbers}"
            ) == "OK":

            if self.work_in_production.get():
                if Messagebox.okcancel(title="Achtung!", message="Änderungen im Produktivsystem - Bitte nochmal bestätigen!") == "OK":
                    self.apply_button_disable()
                else:
                    self.clear_input()
            else:
                self.apply_button_disable()
                # Run Program
        else:
            self.clear_input()       

    def apply_button_disable(self):
        # disable Button
        self.apply_button["state"] = tk.DISABLED # um sicherzustellen, dass der Button nur einmal gedrückt wird.
        self.apply_infotext.config(text="Änderungen werden durchgeführt...")
    
    def process_input(self):
        # Process input (AKNrs and Roles List)
        self.akNumbers = re.findall("AK\d{6}", self.input_form.users_text.get(1.0, tk.END))
        for num, var in enumerate(self.input_form.checkbuttons_var):
            # translates the true/false list in roles
            if var.get():
                self.roles_list.append(self.display_roles_list[num])# = [var.get() for var in self.input_form.checkbuttons_var]
    
    def clear_input(self):
        self.akNumbers = []
        self.roles_list = []

    
class Input_Form(tk.Frame):

    # GRID LAYOUT
    # -------------------------------------------------------------
    # Checkbox if work in production or sandbox
    # Select users                          | Ad Roles
    # text indput (copy/paste list of AKNr) | Checkboxes of roles
    # Apply Button
    # -------------------------------------------------------------

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