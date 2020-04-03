#if en elif schema maken en dan invullen met pass



getal = int(input('Geef een willekeurig getal: '))

if getal < 0 and getal % 2 ==0:
    uitvoer = 'negatief en even'

elif getal < 0 and getal % 2 !=0:
    uitvoer = 'negatief en oneven'

elif getal > 0 and getal % 2 == 0:
    uitvoer = 'positief en even'

elif getal > 0 and getal % 2 != 0:
    uitvoer = 'positief en oneven'

else:
    uitvoer = 'het getal is 0'

print(uitvoer)
