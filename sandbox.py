# import re
# with open("input_rolesProfiles.txt", "r") as i:
#     # lines = i.readlines()
#     inputfile = i.read()
#     lines = re.findall("roles_\w*", inputfile)
# print(lines)

# import matplotlib.pyplot as plt

# fig, ax = plt.subplots()
# for i in range(5):
#     myCircle = plt.Circle((0.5, 0.5), i/10, fill=False)
#     ax.add_artist(myCircle)
# plt.title( 'Circle' )
# plt.show()


# from datetime import datetime
# # current dateTime
# now = datetime.now()

# # convert to string
# date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
# print('DateTime String:', date_time_str)

import sys

testing = True

if testing:
    x = input("y/N")
    if x=="y":
        pass
    else:
        sys.exit()

print("normal stuff")