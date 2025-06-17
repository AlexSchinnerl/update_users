from gui import Roles_GUI, Info_Window
from utils import getAPIkey, load_roles, modify_roles, update_roles

import os

def main():
    roles = Roles_GUI()
    roles.mainloop()
    # after window terminated get inputs out of class instance
    # akNumbers = roles.akNumbers
    # roles_list = roles.roles_list
    # work_in_production = roles.work_in_production.get()

    # print(work_in_production, roles_list, akNumbers)

    # start info Window


    # start "old" main
    # counter = 0
    # for akNR in akNumbers:
    #     url, key = getAPIkey(akNR, work_in_production)
    #     base_root = load_roles(akNR, url)

    #     if not roles_list:
    #         # if no roles specified - only load Roles profile (skip modify roles)
    #         continue

    #     modified_root = modify_roles(akNR, base_root, roles_list)
    #     update_roles(akNR, modified_root, key)
    #     counter += 1
    #     print(f"{counter} user(s) updated")
    #     print("---------------------------")



if __name__ == "__main__":
    main()

