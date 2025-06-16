import tkinter as tk
import ttkbootstrap as tb
from pathlib import Path

from .gui_input_form import Input_Form
from .gui_apply_button import Apply_Button
from .gui_const import STANDARD_FONT, WINDOW_SIZE
# from .info_window import Info_Window

# https://www.youtube.com/watch?v=X5yyKZpZ4vU
# https://www.youtube.com/watch?v=aAk3ORDr63U

# Wenn die Function nur für Frame relevant, dann in der Frame Klasse anlegen. Wenn relevant für die ganze App, dann in der Main_App

# Class that creates the most basic app

    # GRID LAYOUT
    # -------------------------------------------------------------
    # Checkbox if work in production or sandbox
    # Select users                          | Ad Roles
    # text indput (copy/paste list of AKNr) | Checkboxes of roles
    # Apply Button
    # -------------------------------------------------------------


class Roles_GUI(tk.Tk):
    def __init__(self):
        super().__init__() # super().__init__() run constructor of tk.Tk (gleich wie root=tkTk()) D.h. die Klasse gibt uns schon eine Instanz von Tk
        # Das erlaubt uns z.b. self.title zu schreiben anstatt zuerst root = tk.TK().
        # hier braucht man nichts, weil GUI die Parent App ist - In der Child Klasse kommt hier der Parent rein.

        # Window Stuff ---------------------------------------------------------------------

        # Title, icon, size, Style
        self.title("Update User Roles")
        # self.iconbitmap()
        self.geometry(WINDOW_SIZE)
        # self.attributes("-fullscreen", True)
        # self.style = tb.Style(theme="superhero")
        self.style = tb.Style(theme="darkly")
        
        # ---------------------------------------------------------------------

        # Variables ---------------------------------------------------------------------
        
        # Load xml files in List for display
        path = Path("roles_xml")
        self.display_roles_list = [file.stem for file in path.rglob("*.xml")]

        # init work in production variable
        self.work_in_production = tk.BooleanVar()

        # AK Nums and roles list to fill later
        self.akNumbers = []
        self.roles_list = []

        # ---------------------------------------------------------------------

        # GUI Puzzle Pieces ---------------------------------------------------------------------
        
        # Input Frame (Form)
        self.input_form = Input_Form(self)

        # Checkbox if work in production
        self.production_checker = tk.Checkbutton(self, text="Änderungen im Produktivsystem?", variable=self.work_in_production, font=STANDARD_FONT)
        self.production_checker.pack(pady=20)

        # Apply Button
        self.apply_button = Apply_Button(self)

        # ---------------------------------------------------------------------
    
