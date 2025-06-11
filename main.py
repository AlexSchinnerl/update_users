from gui_classes import Roles_GUI

import requests
import xml.etree.ElementTree as ET
from datetime import datetime

from utils import getAPIkey


def loader(akNR, url):
    response = requests.get(url)
    root = ET.fromstring(response.content)

    # save response for checking
    now = datetime.now()
    now_formated = now.strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"saveFiles/{akNR}_Role_Profile_{now_formated}.xml", "w", encoding="UTF-8") as f:
        f.write(response.text)
    
    print("loaded")
    
    return root

def main():
    roles = Roles_GUI()
    roles.mainloop()
    # after window terminated get inputs out of class instance
    akNumbers = roles.akNumbers
    roles_list = roles.roles_list
    work_in_production = roles.work_in_production.get()

    print(akNumbers, roles_list, work_in_production)

    # start "old" main
    counter = 0
    for akNR in akNumbers:
        url, key = getAPIkey(akNR, work_in_production)
        # base_root = loader(akNR, url)

        # if loader break here


        # modified_root = modify_roles(akNR, base_root, roles_list)
        # updater(akNR, modified_root, key)
        counter += 1
        print(f"{counter} user(s) updated")
        print("---------------------------")



if __name__ == "__main__":
    main()

