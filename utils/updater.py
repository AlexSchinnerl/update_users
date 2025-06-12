import requests
import xml.etree.ElementTree as ET

def update_roles(akNR, root, key):
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
