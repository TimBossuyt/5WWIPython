bereik = int(input('Hoeveel getallen: '))

#lees het eerste getal voor de lus in

getal0 = int(input('Geef een getal: '))
#het eerste getal is onmiddelijk de som en het grootste getal

som, grootste = getal0, getal0


for i in range(bereik - 1):
    getal = int(input('Geef een getal: '))
    som += getal
    grootste = max(grootste, getal)


gemiddelde = som/bereik

uitvoer = 'Het grootste getal is {} en het gemiddelde is {:.2f}'

print(uitvoer.format(grootste, gemiddelde))
