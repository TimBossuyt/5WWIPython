dikte = int(input('De dikte vh. papier: '))

vouwen = 0

hoogte = dikte

afstand = int(input('Afstand tot een hemellichaam: '))

while hoogte < afstand:
    hoogte *= 2
    vouwen += 1

uitvoer = 'Na {} keer vouwen bedraagt de dikte van het papier {} mm.'

print(uitvoer.format(vouwen, hoogte))
