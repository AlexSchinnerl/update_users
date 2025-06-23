
from utils import getAPIkey, load_roles, modify_roles, update_roles
from gui.gui_utils import update_textbox
from gui.gui_infoscreen import InfoScreen

def run_program(parent):
    counter = 0
    max_users = len(parent.akNumbers)
    info_screen = InfoScreen(parent, max_users)
    
    # infoscreen.infoscreen.percent_bar.maximum = len(infoscreen.akNumbers)
    for akNR in parent.akNumbers:
        update_textbox(info_screen, f"Working on User: {akNR}\n")
        url, key = getAPIkey(akNR, parent.work_in_production)
        base_root = load_roles(akNR, url, info_screen)

        if len(parent.roles_list) > 0:
            # if no roles specified - only load Roles profile (skip modify roles)
            modified_root = modify_roles(akNR, base_root, parent.roles_list, info_screen)
            update_roles(akNR, modified_root, key, info_screen)

        counter +=1
        info_screen.finish_user_update(counter, max_users)


# def finish_user_update(infoscreen, counter, max_users):
#     infoscreen.percent_bar.mask = f"User verarbeitet: {counter}/{max_users}"
#     infoscreen.percent_bar.step(1)
#     infoscreen.infotext.insert(tk.INSERT, f"{counter} user(s) processed\n")
#     infoscreen.infotext.insert(tk.INSERT, "---------------------------\n")
#     infoscreen.update()
     