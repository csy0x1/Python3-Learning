def normalize(name):
    return str.title(name)


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
