getal = float(input('Geef een getal tussen 0 en 1'))

som = 0
aantal_termen = 0
breuk = 0.5

while som < getal:
    som += breuk
    breuk *= 0.5
    aantal_termen += 1

uitvoer = '{} {}'

print(aantal_termen, som)


