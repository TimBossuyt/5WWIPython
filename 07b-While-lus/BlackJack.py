kaart = int(input('Geef een kaart: '))

totaal = kaart

while totaal < 21 and kaart != 0:
    kaart = int(input('Geef een kaart: '))
    totaal += kaart


if totaal == 21:
    uitvoer = 'Gewonnen!'
    print(uitvoer)

elif totaal > 21:
    uitvoer = 'Verbrand ({})'
    print(uitvoer.format(totaal))

else:
    uitvoer = 'Voorzichtig gespeeld ({})'
    print(uitvoer.format(totaal))
