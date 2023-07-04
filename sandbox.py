import re
with open("input_rolesProfiles.txt", "r") as i:
    # lines = i.readlines()
    inputfile = i.read()
    lines = re.findall("roles_\w*", inputfile)
print(lines)