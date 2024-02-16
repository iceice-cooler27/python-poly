#Name: Chia Wei En Wayne
#ID: S10257584G
#Date: 8 July 2023
#Status: Completed, Checked

#Read File
path = "C:\\1.1\\Text Files\\"
colourfile = open(path + "colors.csv", "r")

colors_dict = {}

data = colourfile.read()
data = data.split("\n")
colourfile.close()

for n in data:
    n = n.split(",")
    key = n[0]
    color = n[1]
    colour_dict = {"{}".format(key):"{}".format(color)}
    colors_dict.update(colour_dict)
print(colors_dict)

new_colors = {}
colour_list = []
for i in colors_dict.values():
    if i not in colour_list:
        colour_list.append(i)
        name_list = []
        for p in colors_dict:
            if colors_dict.get(p) == i:
                name_list.append(p)
        new_dict = {"{}".format(i):name_list}
        new_colors.update(new_dict)
print()
print(new_colors)

"""
colors_dict = {}
new_colors = {}

filename = "colors.csv"
file = open(path + filename, "r")

for line in file:
    line = line.strip("\n")
    data_list = line.split(",")

    colors_dict[data_list[0]] = data_list[1]
file.close()

for name in colors_dict:
    color = colors_dict[name]
    name_list = []
    if color in new_colors:
        name_list = new_colors[color]
    name_list.append(name)
    new_colors[color] = name_list

print(colors_dict)
print(new_colors)
"""
