def n_gram(a, n):
    result = []
    for i in range(0, len(a) - n + 1):
        result.append(a[i:i + n])

    return result

set_X = set(n_gram('paraparaparadise', 2))
set_Y = set(n_gram('paragraph', 2))
print(str(set_X))
print(str(set_Y))

set_or = set_X | set_Y
print(str(set_or))

set_and = set_X & set_Y
print(str(set_and))

set_sub = set_X - set_Y
print(str(set_sub))

print(str('se' in set_X))
print(str('se' in set_Y))
