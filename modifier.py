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

def modify_roles(akNR, root, roles_list):
    # delete all roles
    roles = root.find("user_roles")
    root.remove(roles)

    print("roles removed")

    # new_roles = ET.parse("user_Roles_2_change.xml")
    # new_root = new_roles.getroot()
    role_profile = build_role_profile(roles_list)
    root.append(role_profile)

    print("user Roles applied")

    tree = ET.ElementTree(root)
    tree.write(f"outputFiles/output_{akNR}.xml")

    print("output written")

    return root