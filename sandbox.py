# build Role Profile

# load user Roles xml
# append other user Roles
# repeat until finish

import xml.etree.ElementTree as ET



def appendRoles(filename, root):
    roles2append = ET.parse(f"{filename}.xml")
    roles2append = roles2append.getroot()
    for child in roles2append:
        root.append(child)

def build_role_profile(profiles_list):
    base_roles = ET.parse(f"{profiles_list[0]}.xml")
    base_root = base_roles.getroot()

    for profile in profiles_list[1:]:
        appendRoles(profile, base_root)
    
    return base_root

roles_list = ["user_Roles_2_change"]
role_profile = build_role_profile(roles_list)

for child in role_profile:
    print(child.tag)