import tkinter as tk

from utils import getAPIkey, load_roles, modify_roles, update_roles

def run_program(infoscreen, akNumbers, roles_list, work_in_production):
    counter = 0
    infoscreen.percent_bar.maximum = len(akNumbers)
    for akNR in akNumbers:
        update_textbox(infoscreen, f"Count: {counter}\n")
        url, key = getAPIkey(akNR, work_in_production)
        base_root = load_roles(akNR, url)
        update_textbox(infoscreen, f"{akNR}: {url}\n")

        if len(roles_list) > 0:
            # if no roles specified - only load Roles profile (skip modify roles)
            modified_root = modify_roles(akNR, base_root, roles_list)
            update_roles(akNR, modified_root, key)

        counter +=1
        finish_user_update(infoscreen, counter)




def config_progressbar(infoscreen, akNumbers):
    infoscreen.percent_bar["maximum"] = len(akNumbers)

def update_textbox(infoscreen, text_2_insert):
    infoscreen.infotext.insert(tk.INSERT, text_2_insert)
    infoscreen.update()

def finish_user_update(infoscreen, counter):
    infoscreen.percent_bar.step(1)
    # infoscreen.percent_bar.config(value = counter) 
    infoscreen.infotext.insert(tk.INSERT, f"{counter} user(s) updated\n")
    infoscreen.infotext.insert(tk.INSERT, "---------------------------\n")
    infoscreen.update()
     
     