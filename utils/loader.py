import requests
import xml.etree.ElementTree as ET
from datetime import datetime

from gui.gui_utils import update_textbox


def load_roles(akNR, url, infoscreen):
    response = requests.get(url)
    root = ET.fromstring(response.content)

    # save response for checking
    now = datetime.now()
    now_formated = now.strftime("%Y-%m-%d_%H-%M-%S")
    filepath = f"saveFiles/{akNR}_Role_Profile_{now_formated}.xml"
    with open(filepath, "w", encoding="UTF-8") as f:
        f.write(response.text)
    
    update_textbox(infoscreen, f"Loaded Profile\nSaved under: {filepath}\n")
    
    return root


# with open("input_akNumbers.txt", "r") as i:
#     usersInput = i.read()
#     akNumbers = re.findall("AK\d{6}", usersInput)

# for akNR in akNumbers:
#     url, key = getAPIkey(akNR)
#     loader(akNR, url)