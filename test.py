import tkinter as tk

from utils import getAPIkey, load_roles, modify_roles, update_roles
from gui.gui_utils import update_textbox

def run_program(infoscreen, akNumbers, roles_list, work_in_production):
    counter = 0
    infoscreen.percent_bar.maximum = len(akNumbers)
    for akNR in akNumbers:
        update_textbox(infoscreen, f"Working on User: {akNR}\n")
        url, key = getAPIkey(akNR, work_in_production)
        base_root = load_roles(akNR, url, infoscreen)

        if len(roles_list) > 0:
            # if no roles specified - only load Roles profile (skip modify roles)
            modified_root = modify_roles(akNR, base_root, roles_list, infoscreen)
            update_roles(akNR, modified_root, key, infoscreen)

        counter +=1
        finish_user_update(infoscreen, counter, akNumbers)


def finish_user_update(infoscreen, counter, akNumbers):
    infoscreen.percent_bar.mask = f"{counter}/{len(akNumbers)}"
    infoscreen.percent_bar.step(1)
    # infoscreen.percent_bar.config(value = counter) 
    infoscreen.infotext.insert(tk.INSERT, f"{counter} user(s) updated\n")
    infoscreen.infotext.insert(tk.INSERT, "---------------------------\n")
    infoscreen.update()
     
     