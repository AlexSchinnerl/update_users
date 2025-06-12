import requests
import xml.etree.ElementTree as ET
from datetime import datetime


def load_roles(akNR, url):
    response = requests.get(url)
    root = ET.fromstring(response.content)

    # save response for checking
    now = datetime.now()
    now_formated = now.strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"saveFiles/{akNR}_Role_Profile_{now_formated}.xml", "w", encoding="UTF-8") as f:
        f.write(response.text)
    
    print("loaded")
    
    return root


# with open("input_akNumbers.txt", "r") as i:
#     usersInput = i.read()
#     akNumbers = re.findall("AK\d{6}", usersInput)

# for akNR in akNumbers:
#     url, key = getAPIkey(akNR)
#     loader(akNR, url)