from math import floor, pi


straal_klein = float(input('Geef de straal van de kleine cirkel? '))
straal_groot = float(input('Geef de straal van de grote cirkel? '))

#berekening

aantal_cirkels = floor(0.83 * (pow(straal_groot, 2)/pow(straal_klein, 2)) - 1.9)

oppervlakte_klein = aantal_cirkels * (pi * pow(straal_klein, 2))

oppervlakte_groot = pi * pow(straal_groot, 2)

bedekkingsgraad = (oppervlakte_klein  / oppervlakte_groot) * 100

#uitvoer
uitvoer = '{} kleine cirkels bedekken {:.2f}% van de grote cirkel'

print(uitvoer.format(aantal_cirkels, bedekkingsgraad))
