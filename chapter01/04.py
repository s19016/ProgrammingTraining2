import re

a = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
b =  re.split(r"\s", re.sub(r",|\.", "",a)) 

c = {}
for (i, word) in enumerate(b):
    n = i + 1 
    if n in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
    	c[word[:1]] = n
    else:
        c[word[:2]] = n
print(c)
