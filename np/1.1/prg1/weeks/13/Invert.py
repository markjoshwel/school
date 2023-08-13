# Invert dictionary: Invert.py
# Mark Joshwel - SXXXXXXXX (IM02/P12)

colors_dict = {}

with open("colors.csv", "r", encoding="utf-8") as cfd:
    colors = cfd.read().splitlines()
    for line in colors:
        # 'Tom,Red'
        name, color = line.split(",")
        colors_dict[name] = color

new_colors = {}
for name, color in colors_dict.items():
    if color not in new_colors:
        new_colors[color] = []
    new_colors[color].append(name)

print(new_colors)
