import tkinter as tk
from ttkbootstrap.dialogs import Messagebox

STANDARD_FONT = ("Arial", 14)
TITLE_FONT = ("Arial", 18)

WINDOW_SIZE = ("900x500")
INFOSCREEN_WINDOW_SIZE = ("500x500")

def update_textbox(infoscreen, text_2_insert):
    infoscreen.infotext.insert(tk.INSERT, text_2_insert)
    infoscreen.update()

def confirmation_message(gui_class):
    input_confirmation = False
    # Zusammenfassung was durchgeführt wird.
    message_string = str(
        f"Folgende Änderungen werden durchgeführt:\n"+
        f"Rollen: {gui_class.roles_list}\n"+
        f"Angewendet auf {gui_class.akNumbers}\n"+
        f"Änderungen werden durchgeführt in: {'Produktivsystem' if gui_class.work_in_production.get() else 'Sandbox'}"
    )
    if Messagebox.okcancel(title="Zusammenfassung", message=message_string) == "OK":
        if gui_class.work_in_production.get() and Messagebox.okcancel(title="Achtung!", message="Änderungen im Produktivsystem - Bitte nochmal bestätigen!") == "OK":
            input_confirmation = True
        elif gui_class.work_in_production.get() == False:
            input_confirmation = True

    return input_confirmation