import re

with open("input.txt", "r") as i:
    inputfile = i.read()
    akNumbers = re.findall("AK\d{6}", inputfile) # find AK Numbers in input file
    print(akNumbers)

for i in akNumbers:
    print(i)