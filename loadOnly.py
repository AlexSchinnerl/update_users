import re
from main import getAPIkey, loader

with open("input_akNumbers.txt", "r") as i:
    usersInput = i.read()
    akNumbers = re.findall("AK\d{6}", usersInput)

for akNR in akNumbers:
    url, key = getAPIkey(akNR)
    loader(akNR, url)