import requests
import xml.etree.ElementTree as ET
from gui.gui_utils import update_textbox

def update_roles(akNR, root, key, infoscreen):
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


    update_textbox(infoscreen, f"user {akNR} updated\n")
