def musbat_nuqtalar(nuqtalar):
    return [(abs(x), abs(y)) for x, y in nuqtalar]

nuqtalar = [(1, -2), (-3, 4), (0, -5), (6, 7)]
print(musbat_nuqtalar(nuqtalar))
