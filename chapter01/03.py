import re

a = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
b = re.split(r"\s", re.sub(r",|\.", "",a))

c = []
for i in b:
    c.append(len(i))
print(c)

