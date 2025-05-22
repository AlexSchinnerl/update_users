import keyring
import requests
import xml.etree.ElementTree as ET
import re
import sys
from datetime import datetime
from modifier import modify_roles

work_in_production = False

def getAPIkey(akNR):
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

def updater(akNR, root, key):
    headers = {
        "accept": "application/json",
        "Content-Type": "application/xml",
    }

    params = {
        "user_id_type": "all_unique",
        "send_pin_number_letter": "false",
        "recalculate_roles": "false",
        "registration_rules": "false",
        "apikey": {key}
    }

    data = ET.tostring(root)
    requests.put(
        f"https://api-eu.hosted.exlibrisgroup.com/almaws/v1/users/{akNR}",
        params=params,
        headers=headers,
        data=data,
    )

    print(f"user {akNR} updated")


def main():

    with open("input_akNumbers.txt", "r") as i:
        usersInput = i.read()
        akNumbers = re.findall("AK\d{6}", usersInput)
    
    with open("input_rolesProfiles.txt", "r") as i:
        rolesInput = i.read()
        roles_list = re.findall("roles_\w*", rolesInput)

    counter = 0
    for akNR in akNumbers:
        url, key = getAPIkey(akNR)
        base_root = loader(akNR, url)
        modified_root = modify_roles(akNR, base_root, roles_list)

        updater(akNR, modified_root, key)
        
        counter += 1
        print(f"{counter} user(s) updated")
        print("---------------------------")

if work_in_production:
    proceed = input("Cave! Working in Production! - Proceed? (y/N)")
    if proceed.lower() == "y":
        pass
    else:
        sys.exit()
        


if __name__ == "__main__":
    main()