import xml.etree.ElementTree as ET
from gui.gui_utils import update_textbox

def appendRoles(filename, root):
    roles2append = ET.parse(f"roles_xml/{filename}.xml")
    roles2append = roles2append.getroot()
    for child in roles2append:
        root.append(child)

def build_role_profile(profiles_list):
    base_roles = ET.parse(f"roles_xml/{profiles_list[0]}.xml")
    base_root = base_roles.getroot()

    for profile in profiles_list[1:]:
        appendRoles(profile, base_root)
    
    return base_root

def modify_roles(akNR, root, roles_list, infoscreen):
    # delete all roles
    roles = root.find("user_roles")
    root.remove(roles)

    update_textbox(infoscreen, f"Old Roles removed\n")

    role_profile = build_role_profile(roles_list)
    root.append(role_profile)

    update_textbox(infoscreen, f"New Role Profile built\n")

    tree = ET.ElementTree(root)
    output_file = f"outputFiles/output_{akNR}.xml"
    tree.write(output_file)

    update_textbox(infoscreen, f"New Role Profile saved under: {output_file}\nReady to update user...\n")

    return root