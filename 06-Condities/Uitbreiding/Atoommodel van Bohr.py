aantal_elektronen = int(input('Geef het aantal elektronen tussen 1 en 156: '))


#berekening
if aantal_elektronen - 124 > 0:
    schil = 'Q'

elif aantal_elektronen - 92 > 0:
    schil = 'P'

elif aantal_elektronen - 60 > 0:
    schil = 'O'

elif aantal_elektronen - 28 > 0:
    schil = 'N'

elif aantal_elektronen - 10 > 0:
    schil = 'M'

elif aantal_elektronen - 2 > 0:
    schil = 'L'

else:
    schil = 'K'


#invoer
uitvoer = 'The {}-shell is the outer shell of a stable atom with {} electrons.'

uitvoer.format(schil, aantal_elektronen)

print(uitvoer.format(schil, aantal_elektronen))

