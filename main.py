import keyring
import requests
import xml.etree.ElementTree as ET
import re
from modifier import modify_roles

def getAPIkey(akNR):
    # key = keyring.get_password("alma_api", "alx_prod").rstrip()
    key = keyring.get_password("alma_api", "alx_sand").rstrip()
    base = "https://api-eu.hosted.exlibrisgroup.com"
    # url = f"{base}/almaws/v1/users/{akNR}?user_id_type=all_unique&view=full&expand=none&apikey={key}"
    url = f"{base}/almaws/v1/users/{akNR}?user_id_type=all_unique&send_pin_number_letter=false&recalculate_roles=false&registration_rules=false&apikey={key}"

    return url, key


def loader(akNR, url):
    response = requests.get(url)
    root = ET.fromstring(response.content)

    # save response for checking
    with open(f"saveFiles/response_{akNR}.xml", "w", encoding="UTF-8") as f:
        f.write(response.text)
    
    print("loaded")
    
    return root


# def modifier(akNR, root):
#     # delete all roles
#     roles = root.find("user_roles")
#     root.remove(roles)

#     print("roles removed")

#     new_roles = ET.parse("user_Roles_2_change.xml")
#     new_root = new_roles.getroot()
#     root.append(new_root)

#     print("user Roles applied")

#     tree = ET.ElementTree(root)
#     tree.write(f"outputFiles/output_{akNR}.xml")

#     print("output written")

#     return root


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
        inputfile = i.read()
        akNumbers = re.findall("AK\d{6}", inputfile) # find AK Numbers in input file
    
    with open("input_rolesProfiles.txt", "r") as i:
        inputfile = i.read()
        # akNumbers = re.findall("AK\d{6}", inputfile) # find AK Numbers in input file
    roles_list = ["roles_circulationDesk_only"]

    # akNumbers = ["AK114820"]
    counter = 0
    for akNR in akNumbers:
        url, key = getAPIkey(akNR)
        base_root = loader(akNR, url)
        modified_root = modify_roles(akNR, base_root, roles_list)

        updater(akNR, modified_root, key)
        
        counter += 1
        print(f"{counter} user(s) updated")
        print("---------------------------")

if __name__ == "__main__":
    main()
