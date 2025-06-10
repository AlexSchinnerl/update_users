from gui_classes import Roles_GUI

import keyring
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

def getAPIkey(akNR, work_in_production):
    if work_in_production:
        key = keyring.get_password("alma_api", "alx_prod").rstrip()
    else:
        key = keyring.get_password("alma_api", "alx_sand").rstrip()
    base = "https://api-eu.hosted.exlibrisgroup.com"
    # url = f"{base}/almaws/v1/users/{akNR}?user_id_type=all_unique&view=full&expand=none&apikey={key}"
    url = f"{base}/almaws/v1/users/{akNR}?user_id_type=all_unique&send_pin_number_letter=false&recalculate_roles=false&registration_rules=false&apikey={key}"

    return url, key

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
    akNumbers = roles.input_form.akNumbers
    roles_list = roles.input_form.roles_list
    work_in_production = roles.work_in_production.get()

    # start "old" main
    counter = 0
    for akNR in akNumbers:
        url, key = getAPIkey(akNR, work_in_production)
        base_root = loader(akNR, url)
        # modified_root = modify_roles(akNR, base_root, roles_list)
        # updater(akNR, modified_root, key)
        
        counter += 1
        print(f"{counter} user(s) updated")
        print("---------------------------")



if __name__ == "__main__":
    main()

