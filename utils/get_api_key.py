import keyring

def getAPIkey(akNR, work_in_production):
    if work_in_production:
        key = keyring.get_password("alma_api", "alx_prod").rstrip()
    else:
        key = keyring.get_password("alma_api", "alx_sand").rstrip()
    base = "https://api-eu.hosted.exlibrisgroup.com"
    # url = f"{base}/almaws/v1/users/{akNR}?user_id_type=all_unique&view=full&expand=none&apikey={key}"
    url = f"{base}/almaws/v1/users/{akNR}?user_id_type=all_unique&send_pin_number_letter=false&recalculate_roles=false&registration_rules=false&apikey={key}"

    return url, key