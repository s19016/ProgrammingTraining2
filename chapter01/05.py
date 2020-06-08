a = "I am an NLPer"
alist = a.split()
b = ''.join(alist)

n =2 

c = []
d = []
for i in range(len(alist) - 1):
    c += [''.join(alist[i:i + n])]

for i in range(len(b) - 1):
    d += [b[i:i + n]]

print(c)
print(d)
