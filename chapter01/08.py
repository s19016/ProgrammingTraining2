def a (string):
    result = ''

    for i in range(0, len(string)):
        if string[i].islower():
            result += chr(219-ord(string[i]))
        else:
            result += string[i]

    return result

print(a("I Have A Apple"))     
print(a("I Hzev A Akkov"))     
