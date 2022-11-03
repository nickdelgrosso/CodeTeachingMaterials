def balanced_latin_squares(n):
    l = [[((j/2+1 if j%2 else n-j/2) + i) % n  for j in range(n)] for i in range(n)]
    if n % 2:  # Repeat reversed for odd n
        l += [seq[::-1] for seq in l]
    return l

def named_latin_squares(names):
    return [[names[e] for e in el] for el in balanced_latin_squares(len(names))]
    
