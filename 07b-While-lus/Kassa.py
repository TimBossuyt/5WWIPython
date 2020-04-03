prijs = float(input('Kostprijs: '))
totaal = 0

while prijs != 0:
    totaal += prijs
    prijs = float(input('Kostprijs: '))

uitvoer = 'De totale prijs is € {:.2f}'

print(uitvoer.format(totaal))
