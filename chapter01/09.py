def test(a):
    a_list = a.split()
    b = []
    
    for i in a_list:
        if len(i) <= 4:
            b.append(i)
        else:
            front = i[0] ; end = i[-1] ; middle = [character for character in i[1:-1]] 
            random.shuffle(middle) 
            randomized = "".join([front, "".join(middle), end]) 
            b.append(randomized)
            
    return " ".join(b)


